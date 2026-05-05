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

## Checkers Ruleset

The game follows American checkers (English draughts) rules. The specific choices below are binding for the MVP and must not be second-guessed during implementation.

### Board and Square Conventions

- The board is 8×8. Only the 32 dark squares are used for play.
- The coordinate system uses `(row, col)` pairs where row 0 is the top of the screen and row 7 is the bottom. Column 0 is the left edge and column 7 is the right edge.
- A square at `(row, col)` is a dark (playable) square when `(row + col)` is odd.
- The lower-left corner of the screen is `(7, 0)`, which is a dark square.
- Player 1 (Red) occupies the bottom of the board and starts at rows 5–7. Player 2 (Black) occupies the top and starts at rows 0–2.
- Player 1's starting squares: `(7,1)`, `(7,3)`, `(7,5)`, `(7,7)`, `(6,0)`, `(6,2)`, `(6,4)`, `(6,6)`, `(5,1)`, `(5,3)`, `(5,5)`, `(5,7)`.
- Player 2's starting squares: `(0,1)`, `(0,3)`, `(0,5)`, `(0,7)`, `(1,0)`, `(1,2)`, `(1,4)`, `(1,6)`, `(2,1)`, `(2,3)`, `(2,5)`, `(2,7)`.
- Each player begins with 12 pieces.

### Men Movement

- A man moves diagonally forward one square at a time to an unoccupied dark square.
- Player 1 (Red) men move toward decreasing row (up the screen, toward row 0).
- Player 2 (Black) men move toward increasing row (down the screen, toward row 7).
- A man may not move backward.

### King Movement

- A king moves diagonally one square at a time in any of the four diagonal directions.
- A king is otherwise subject to the same capture and mandatory-capture rules as a man.

### Captures

- A piece captures by jumping diagonally over an adjacent opponent piece to the empty square immediately beyond it.
- The captured piece is removed from the board at the end of the full move (after all jumps in a sequence are complete).
- A man may only capture in its forward diagonal directions. A king may capture in all four diagonal directions.

### Mandatory Capture

- If one or more captures are available to the active player, that player must capture on their turn.
- When multiple pieces can capture, the player may freely choose which piece to move.
- There is no requirement to choose the sequence that captures the maximum number of pieces. The player picks any legal capture.

### Multi-Jump Sequencing

- After completing a capture, if the jumping piece has at least one additional capture available from its new position, the player must continue jumping with the same piece.
- The turn ends only when no further captures are available for the jumping piece.
- The player may not abandon a jump sequence mid-way to move a different piece.

### Promotion Timing

- A man is promoted to king immediately when it lands on any square in the opponent's back row.
  - Player 1 (Red) is promoted on row 0.
  - Player 2 (Black) is promoted on row 7.
- **If a man reaches the back row as part of a multi-jump sequence, the sequence stops at that point.** The piece is crowned and the turn ends. The newly promoted king may not continue jumping in the same turn.

### Win Conditions

- A player wins when their opponent has no legal move at the start of the opponent's turn.
- This occurs when the opponent has no pieces remaining, or all remaining opponent pieces are completely blocked.
- There is no time limit or move limit enforced in the MVP.

### Draw Handling

- The MVP does not enforce automatic draw conditions (no fifty-move rule, no repetition detection).
- Players may agree to a draw by mutual consent using the in-game draw-offer UI if it is implemented; otherwise draws are not tracked.
- Draw handling beyond this is deferred to a future issue.

### Restart Flow

- When a win condition is detected the application presents both players with a clear prompt to start a new game.
- Accepting the restart resets the board to the standard 12-vs-12 starting position described above, clears all piece state, and returns to Player 1's first turn.
- The game may also be restarted at any point before a winner is decided if both players agree; the mechanism for this is deferred to a future issue.
- Save and load are out of scope for the MVP.

## Deferred Clarifications

These topics are intentionally left open for future issues and design docs:

- visual presentation details (colors, piece art, board sizing)
- save/load behavior, if any
- in-game draw-offer UI flow
- mid-game restart mechanism
