# BenchmarkGames Erlang benchmarks

This folder contains the Erlang implementations used in the benchmark game case study.
Each benchmark subfolder keeps its original Makefile-based workflow, and the checked-in CSV files are grouped under `results/`.

## Main contents

- `fannkuch-redux/`, `mandelbrot/`, `n-body/`, `reverse-complement/` - benchmark implementations and Makefiles.
- `compile_all.py` - runs the Makefile targets across all Erlang benchmark folders.
- `average.py` and `ratio.py` - small analysis helpers for checked-in CSV outputs.
- `results/` - raw, summary, and derived Erlang benchmark outputs.

## Notes

- Measurement output aggregation writes to `results/` now instead of the folder root.
- Temporary JSON dumps are still produced next to benchmark runs when the Makefiles expect that behavior.
- This folder is active and directly tied to the benchmark game study.
