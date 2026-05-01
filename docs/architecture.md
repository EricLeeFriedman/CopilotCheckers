# Architecture

This document describes the intended architectural direction for the future game code. It is a design contract, not a statement that the implementation already exists.

## Core Architectural Shape

- A small set of C-style modules with explicit APIs
- Plain structs with public fields
- Deterministic update and render flow
- No object-oriented framework layer

## Planned Subsystems

- platform and Win32 message pump
- software renderer
- input and drag interaction
- game state and rules
- UI overlays and restart flow
- test mode and test reporting

## Memory Model

- Reserve memory up front during startup.
- Split memory into arenas owned by major systems.
- Avoid runtime heap allocation in normal execution and tests.
- Make ownership and lifetime obvious at module boundaries.

## Dependency Direction

- Platform layer exposes raw input, timing, and framebuffer access.
- Game logic operates on plain data, independent from rendering details.
- Rendering consumes immutable game state snapshots or read-only views where practical.
- Test mode calls subsystem test entry points directly inside the application.

## Current State

No application code exists yet. This document defines the target shape that future code should follow.
