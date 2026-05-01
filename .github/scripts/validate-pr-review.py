#!/usr/bin/env python3
"""
Offline validation for the PR review workflow logic in .github/workflows/pr-review.yml.

Run this script to verify that:
1. review output parsing behaves deterministically
2. PR routing between code review and process review behaves as expected
"""

import json
import sys

FALLBACK_REVIEW = {
    "event": "REQUEST_CHANGES",
    "body": "@copilot Automated review could not parse structured output. Manual inspection required.",
    "blocking": [],
    "comments": [],
}


def parse_review(text):
    """Parse text as JSON and return a validated review dict."""
    import re

    cleaned = text.replace("\r", "").lstrip("\ufeff")
    cleaned = re.sub(r"\x1b\[[0-9;?]*[ -/]*[@-~]", "", cleaned).strip()

    if cleaned.startswith("```"):
        lines = cleaned.splitlines()
        if len(lines) >= 3:
            cleaned = "\n".join(lines[1:-1]).strip()

    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError:
        start = cleaned.find("{")
        end = cleaned.rfind("}")
        if start >= 0 and end > start:
            try:
                parsed = json.loads(cleaned[start : end + 1])
            except json.JSONDecodeError:
                return dict(FALLBACK_REVIEW)
        else:
            return dict(FALLBACK_REVIEW)

    if not isinstance(parsed, dict):
        return dict(FALLBACK_REVIEW)

    if not isinstance(parsed.get("event"), str):
        return dict(FALLBACK_REVIEW)

    if parsed["event"] not in {"APPROVE", "COMMENT", "REQUEST_CHANGES"}:
        return dict(FALLBACK_REVIEW)

    for key in ("blocking", "comments"):
        if key not in parsed or not isinstance(parsed[key], list):
            return dict(FALLBACK_REVIEW)
        for entry in parsed[key]:
            if not isinstance(entry, dict):
                return dict(FALLBACK_REVIEW)
            for required_key in ("path", "line", "body"):
                if required_key not in entry:
                    return dict(FALLBACK_REVIEW)
            try:
                line_val = int(entry["line"])
            except (ValueError, TypeError):
                return dict(FALLBACK_REVIEW)
            if line_val <= 0:
                return dict(FALLBACK_REVIEW)

    return parsed


def classify_pr(changed_paths):
    """Return review kind and agent name for a pull request."""
    has_code = any(path.startswith("src/") or path == "build.ps1" for path in changed_paths)
    if has_code:
        return {"review_kind": "code", "agent_name": "cpp-pr-review"}
    return {"review_kind": "process", "agent_name": "process-pr-review"}


_PASS = 0
_FAIL = 0


def _check(label, actual, expected):
    global _PASS, _FAIL
    if actual == expected:
        print(f"  PASS  {label}")
        _PASS += 1
    else:
        print(f"  FAIL  {label}")
        print(f"        expected: {expected!r}")
        print(f"        actual:   {actual!r}")
        _FAIL += 1


def test_parse_review_valid_approve():
    payload = {"event": "APPROVE", "body": "@copilot ok", "blocking": [], "comments": []}
    result = parse_review(json.dumps(payload))
    _check("valid APPROVE parses", result["event"], "APPROVE")


def test_parse_review_valid_request_changes():
    payload = {
        "event": "REQUEST_CHANGES",
        "body": "@copilot fix this",
        "blocking": [{"path": "docs/workflow.md", "line": 10, "body": "@copilot update docs"}],
        "comments": [],
    }
    result = parse_review(json.dumps(payload))
    _check("REQUEST_CHANGES parses", result["event"], "REQUEST_CHANGES")
    _check("blocking path preserved", result["blocking"][0]["path"], "docs/workflow.md")


def test_parse_review_invalid_json():
    result = parse_review("not json")
    _check("invalid JSON falls back", result["event"], "REQUEST_CHANGES")


def test_parse_review_invalid_event():
    payload = {"event": "NOPE", "body": "@copilot", "blocking": [], "comments": []}
    result = parse_review(json.dumps(payload))
    _check("invalid event falls back", result["event"], "REQUEST_CHANGES")


def test_parse_review_markdown_fence():
    payload = {"event": "COMMENT", "body": "@copilot note", "blocking": [], "comments": []}
    fenced = f"```json\n{json.dumps(payload)}\n```"
    result = parse_review(fenced)
    _check("fenced JSON parses", result["event"], "COMMENT")


def test_parse_review_invalid_line():
    payload = {
        "event": "COMMENT",
        "body": "@copilot note",
        "blocking": [],
        "comments": [{"path": "AGENTS.md", "line": 0, "body": "@copilot bad line"}],
    }
    result = parse_review(json.dumps(payload))
    _check("non-positive line falls back", result["event"], "REQUEST_CHANGES")


def test_classify_code_pr():
    result = classify_pr(["src/game.cpp", "docs/workflow.md"])
    _check("src path routes to code review", result["agent_name"], "cpp-pr-review")


def test_classify_build_pr():
    result = classify_pr(["build.ps1"])
    _check("build.ps1 routes to code review", result["review_kind"], "code")


def test_classify_process_pr():
    result = classify_pr(["docs/workflow.md", ".github/workflows/pr-review.yml"])
    _check("docs and workflow route to process review", result["agent_name"], "process-pr-review")


def test_classify_empty_pr():
    result = classify_pr([])
    _check("empty file list defaults to process review", result["review_kind"], "process")


def main():
    print("Running PR review validation tests...")
    print()

    print("--- parse_review tests ---")
    test_parse_review_valid_approve()
    test_parse_review_valid_request_changes()
    test_parse_review_invalid_json()
    test_parse_review_invalid_event()
    test_parse_review_markdown_fence()
    test_parse_review_invalid_line()

    print()
    print("--- classify_pr tests ---")
    test_classify_code_pr()
    test_classify_build_pr()
    test_classify_process_pr()
    test_classify_empty_pr()

    print()
    total = _PASS + _FAIL
    print(f"Results: {_PASS}/{total} passed, {_FAIL}/{total} failed.")
    sys.exit(1 if _FAIL else 0)


if __name__ == "__main__":
    main()
