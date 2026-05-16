# RosettaQueens

This folder contains the Rosetta Code N-Queens case study used to compare Erlang implementations and OTP versions.
It keeps the Erlang source files close to the benchmark scripts and groups checked-in outputs under `results/`.

## Main contents

- `queens*.erl`, `n_queens.erl`, and helper Erlang files - benchmark implementations.
- `run_linux.py` - Linux measurement runner using Scaphandre.
- `average.py` and `ratio.py` - small analysis helpers for the CSV outputs.
- `results/` - raw, summary, and derived CSV files kept for reproducibility.
- `archive/` - legacy tests and planning notes.

## Results layout

- `results/raw/` - direct benchmark outputs for OTP and Linux runs.
- `results/summary/` - averaged comparison tables.
- `results/derived/` - ratio tables derived from the raw or summary outputs.

## Notes

- Historical CSV files are intentionally retained because they support paper comparisons and later thesis work.
- Temporary measurement JSON files now belong in `generated/` and are ignored by Git.
- This folder is active, but `archive/` holds older exploratory material that should not clutter the main workflow.
