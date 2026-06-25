# BlockBlastScript

An automated bot that plays Block Blast by reading the
game directly off the screen and controlling the mouse. It uses
[PyAutoGUI](https://pyautogui.readthedocs.io/) to sample pixel colors (to detect the board and the
offered pieces) and to drag pieces onto the board.

> **Note:** This is a screen-scraping bot driven entirely by hardcoded pixel coordinates calibrated
> for one specific display setup. It is a personal/hobby project, not a general-purpose solver — see
> [Calibration](#calibration) and [Limitations](#limitations--known-issues) before running it.

## How it works

The whole program lives in `Code.py` and runs as one continuous loop. Each iteration:

1. **Reads the board.** Samples a pixel at the center of each of the 64 cells (using `XcordToPixel` /
   `YcordToPixel`) on the 8×8 grid and compares it to the previously stored board background color. Filled vs. empty
   is stored in `realBoard` (a list of 64 booleans, indexed `x + 8*y`).
2. **Identifies the three pieces.** Probes a set of marker pixels in each of the three piece
   slots and matches the pattern to one of **41 piece shapes** (the ids are stored in `pieceIDs`). Piece shapes are
   defined in two parallel functions: `updateTestBoard` (updates the test board after a piece has been tested at specific coordinates) and
   `canPieceFit` (tests whether or not a piece can fit at specific coordinates).
3. **Searches for the best plan.** Brute-forces all 6 orderings of the three pieces, and for each
   ordering every position on the grid for each piece (a triple-nested 8×8 scan). Each resulting
   board is scored, and the highest-scoring placement of all three pieces is stored as the best solution.
4. **Execute.** Drags each piece from its slot to the chosen grid cell (`movePieceToBoard`) in the
   best order.

### Scoring heuristic

Candidate boards are ranked by a "happiness factor" (`findHappinessFactor`) plus a large bonus when
the placement clears a line (`testBrokenRows`): clearing a rows/column is weighted far above board
shape, so the bot strongly prefers to get the in game combo and otherwise tries to keep blocks clustered.

### Piece IDs

Pieces are referenced by integer ID (1–41). A few pieces:

- `1` = single cell; `2`/`3` = dominoes; `8`/`9` = 1×3 lines
- `14` = 2×2 square; `31`–`34` = the long 4- and 5-cell bars; `37` = 3×3 square
- `0` = empty slot (incase no piece is in the slot, this happens when the bot misplaces a piece or two due to interference like a text message)

The full mapping is the `if/elif` ladders in `updateTestBoard` and `canPieceFit`.

## Requirements

- **An android phone**
- **[Scrcpy](https://github.com/genymobile/scrcpy)**
- **Python 3** 
- **PyAutoGUI**

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install pyautogui
```

## Running

1. Run scrcpy on computer and enter Block Blast on phone
2. Hover the mouse over a blank tile in Block Blast
3. Run the script and switch to the game within the initial delay:

```bash
python Code.py
```

The bot then loops indefinitely, reading the board and placing pieces on its own.

**To stop it:** trigger PyAutoGUI's fail-safe by placing mouse into a screen corner, or
press `Ctrl+C` in the terminal.

## Calibration

Every screen coordinate in `Code.py` is hardcoded near the top of the file and must match your
display for the bot to work. This is being fixed so that it works for all phone and computer combinations.

## Limitations & known issues

- **Display-specific:** hardcoded coordinates mean it only works on the setup it was calibrated for.
