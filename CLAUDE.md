# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

This repository is in its initial state: it contains only a `README.md` and a Python `.gitignore`. There is no source code, dependency manifest, test suite, or build tooling yet.

**Goal (from the README):** an automated bot/script that plays the game *Block Blast* — likely a screen-capture + board-state + move-solver loop driving simulated input.

The `.gitignore` is the standard GitHub Python template, so this is intended to be a **Python** project. Nothing else about the stack is committed yet, so confirm tooling choices with the user before assuming them.

## When adding the first code

There are no established conventions to follow yet, so the first substantive change effectively sets them. Worth deciding up front and recording back into this file:

- Dependency manager (the `.gitignore` already accounts for pip/pipenv/poetry/pdm/uv) and the run/test commands once they exist.
- For a Block Blast player, expect roughly these concerns to become the architecture — keep them as separate, testable modules:
  - **Capture** — grab the game screen / board region.
  - **Perception** — parse the captured image into a board grid + the set of available pieces.
  - **Solver** — choose placements (the pure, easily unit-tested core; keep it free of I/O).
  - **Actuation** — translate chosen placements into clicks/taps/drags.
- Keep the solver decoupled from capture and actuation so game logic can be tested without a live game.

Update this file with real build/lint/test commands and module layout as soon as they exist.
