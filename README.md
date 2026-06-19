# BlockBlastScript

An automated bot that plays [Block Blast](https://en.wikipedia.org/wiki/Block_Blast) by reading the
game directly off the screen and controlling the mouse. It uses
[PyAutoGUI](https://pyautogui.readthedocs.io/) to sample pixel colors (to detect the board and the
offered pieces) and to drag pieces onto the board.

> **Note:** This is a screen-scraping bot driven entirely by hardcoded pixel coordinates calibrated
> for one specific display setup. It is a personal/hobby project, not a general-purpose solver — see
> [Calibration](#calibration) and [Limitations](#limitations--known-issues) before running it.

## How it works

The whole program lives in `Code.py` and runs as one continuous loop. Each iteration:

1. **Read the board.** Samples a pixel at the center of each of the 64 cells (`XcordToPixel` /
   `YcordToPixel`) on the 8×8 grid and compares it to the board background color. Filled vs. empty
   is stored in `realBoard` (a flat list of 64 booleans, indexed `x + 8*y`).
2. **Identify the three offered pieces.** Probes a set of marker pixels in each of the three piece
   slots and matches the pattern to one of **41 piece shapes** (`pieceIDs`). Piece geometry is
   defined in two parallel functions: `updateTestBoard` (stamp a piece onto a board) and
   `canPieceFit` (test placement legality / bounds).
3. **Search for the best plan.** Brute-forces all **6 orderings** of the three pieces, and for each
   ordering every position on the grid for each piece (a triple-nested 8×8 scan). Each resulting
   board is scored, and the highest-scoring placement of all three pieces is kept.
4. **Execute.** Drags each piece from its slot to the chosen grid cell (`movePieceToBoard`) in the
   winning order.

### Scoring heuristic

Candidate boards are ranked by a "happiness factor" (`findHappinessFactor`) plus a large bonus when
the placement clears lines (`testBrokenRows`): clearing rows/columns is weighted far above board
shape, so the bot strongly prefers line-clearing moves and otherwise tries to keep blocks clustered.

### Piece IDs

Pieces are referenced by integer ID (1–41). A few anchors:

- `1` = single cell ("the dot"); `2`/`3` = dominoes; `8`/`9` = 1×3 lines
- `14` = 2×2 square; `31`–`34` = the long 4- and 5-cell bars; `37` = 3×3 square
- `0` = empty slot (no piece offered)

The full mapping is the `if/elif` ladders in `updateTestBoard` and `canPieceFit`.

## Requirements

- **Python 3** (Windows; coordinates are calibrated for a Windows display)
- **PyAutoGUI**

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install pyautogui
```

## Running

1. Open Block Blast so it is visible on screen at the exact position/resolution the coordinates were
   calibrated for (see below).
2. Run the script and switch to the game within the initial delay:

```bash
python Code.py
```

The bot then loops indefinitely, reading the board and placing pieces on its own.

**To stop it:** trigger PyAutoGUI's fail-safe by quickly slamming the mouse into a screen corner, or
press `Ctrl+C` in the terminal. There is no built-in stop condition.

## Calibration

Every screen coordinate in `Code.py` is hardcoded near the top of the file and must match your
display for the bot to work:

- **Board origin & cell size:** `XcordToPixel` / `YcordToPixel` (`767`/`327` origin, `54` px per cell)
- **Piece-slot markers:** the `left_pointForID*`, `left3x3*`, `left2x3*`, `left3x2*`, `left2x2*`
  constants, with slots spaced `143` px apart
- **Drag targets & UI clicks:** the per-piece `Xto00`/`Yto00` offsets in `movePieceToBoard`, and the
  "reroll/continue" clicks in the main loop

If the game is at a different resolution or window position, these values must be re-measured (e.g.
with `pyautogui.position()`) and updated.

## Limitations & known issues

- **Display-specific:** hardcoded coordinates mean it only works on the setup it was calibrated for.
- **`findHappinessFactor` bug:** the neighbor scan reads the global `XCord`/`YCord` instead of its
  local loop variables, and uses an `elif` chain that checks only one neighbor — so the shape score
  is not computed as intended. Line-clear scoring still dominates, but the heuristic is weaker than
  it looks.
- **No graceful exit / persistence:** runs forever until killed; nothing is saved.
- **Misread recovery is heuristic:** if the same three pieces are detected twice in a row the bot
  assumes its last move failed and nudges the cursor (`errorNum`); this can drift over repeated
  failures.
