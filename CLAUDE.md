# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A PyAutoGUI screen bot that plays the game *Block Blast*. It reads the 8×8 board and the three
offered pieces by sampling screen pixel colors, brute-forces the best placement, and drag-drops the
pieces with the mouse. All logic lives in a single script, `Code.py`.

## Running

There is no build, test, or lint setup — it is one script run directly:

```bash
python -m venv .venv && .venv\Scripts\activate   # Windows
pip install pyautogui                              # the only dependency (not pinned anywhere yet)
python Code.py
```

The game must be open and positioned to match the hardcoded coordinates (see Calibration). The bot
loops forever; stop it with PyAutoGUI's fail-safe (mouse to a screen corner) or `Ctrl+C`.

## Architecture (all in `Code.py`)

The file is organized as: module-level coordinate constants → helper functions → one big
`while` loop ("real program") that drives everything. Key pieces:

- **Board model:** an 8×8 grid stored as a flat 64-element boolean list, indexed `x + 8*y`.
  `realBoard` is the live game state; `testBoard` is a scratch copy mutated during search;
  `bestBoard` holds the best result found. `blockFilled` / `fillTestBlock` / `emptyTestBlock` are
  the accessors (note: `blockFilled` reads `testBoard`, not `realBoard`).
- **Pieces by integer ID (1–41), defined in two parallel ladders that must stay in sync:**
  `updateTestBoard(x, y, id)` stamps a piece onto `testBoard` (and then clears any full rows/columns,
  incrementing the global `testBrokenRows`), and `canPieceFit(x, y, id)` checks bounds + collisions
  for the same shape. **If you add or change a piece, edit both functions** — and the detection
  ladder in the main loop (below).
- **Perception (main loop):** `XcordToPixel`/`YcordToPixel` map grid cells to screen pixels;
  `colorMatch` does tolerant RGB comparison. Pieces are recognized by probing marker pixels in each
  of the three slots (the `left*` constants, slots spaced 143px) and walking an `if/elif` ladder to
  assign each `pieceIDs[slot]`.
- **Search:** six explicit copy-pasted blocks, one per placement order (123, 132, 213, 231, 312,
  321), each a triple-nested 8×8 scan. Every candidate is scored and the global `best*` variables
  (`bestOrder`, `bestP1Xcord`, …) record the winner.
- **Scoring:** `findHappinessFactor` (board-shape heuristic) plus a large constant bonus when the
  move clears lines, so line clears dominate placement choice.
- **Actuation:** `movePieceToBoard(x, y, id, slot)` drag-drops a piece from its slot to a grid cell,
  using per-piece pixel offsets (`Xto00`/`Yto00`).

## Conventions and gotchas specific to this code

- **Coordinates are hardcoded for one display** (board origin `767,327`, 54px cells, 143px slot
  pitch, plus drag offsets and UI clicks in `movePieceToBoard`/main loop). Any resolution or window
  move breaks it; re-measure with `pyautogui.position()`. There is no config layer.
- **Global mutable state is load-bearing.** `testBoard` and `testBrokenRows` are globals mutated by
  `updateTestBoard`/`blockFilled`; the search saves/restores them via `placeHolderBoard*` and
  `helperTestBrokenRows*` copies between piece levels. Be careful refactoring these into parameters.
- **Two case-sensitive coordinate namings coexist:** lowercase `Xcord`/`Ycord` are local loop
  vars; uppercase `XCord`/`YCord` are globals used during board scanning. They are easy to confuse —
  in fact `findHappinessFactor` has a latent bug where it reads the uppercase globals instead of its
  own lowercase loop variables (and uses `elif` so it only ever checks one neighbor). Preserve or fix
  deliberately, don't "tidy" the names blindly.
- The six search blocks are near-identical; a change to scoring or the best-tracking logic must be
  applied to all six.

## When making changes

- Keep `updateTestBoard`, `canPieceFit`, and the piece-detection ladder consistent with each other.
- Prefer verifying piece geometry/scoring by reasoning about the flat-array math rather than running
  the bot, since running requires the live game on a calibrated screen.
- Update `README.md` (which documents behavior, calibration, and known issues) alongside any
  behavioral change.
