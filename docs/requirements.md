# Requirements

## Product Scope

The project is a native Windows checkers game for two players sharing one machine.

## Player-Facing Requirements

- The game must support a full local two-player match.
- Input is mouse-only.
- Piece movement is click-and-drag.
- The application must clearly support restarting after a winner is decided.

## Platform Requirements

- Windows only
- Win32 APIs
- 2D software rendering using the Windows API

## Engineering Constraints

- C++
- C-style module boundaries and plain structs
- Avoid object-oriented architecture
- No third-party libraries
- Avoid the C standard library where practical
- No runtime dynamic allocation
- Pre-reserve memory and divide it into subsystem-specific arenas

## Deferred Clarifications

These topics are intentionally left open for future issues and design docs:

- exact checkers ruleset details beyond the basic restart requirement
- visual presentation details
- board coordinate conventions
- save/load behavior, if any
