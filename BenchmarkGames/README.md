# BenchmarkGames

This folder contains the benchmark game case study used to compare Erlang against other implementations and runtime configurations.
The benchmark source folders are kept close to the original benchmark layout, while analysis outputs are grouped separately.

## Main contents

- `Erlang/` - Erlang benchmark implementations, Makefiles, and Erlang-specific results.
- `compile_all.py` - walks the benchmark folders and runs `make compile`, `make run`, or `make clean`.
- `test.py` - records average runtime per benchmark folder.
- `gen-input.sh` - regenerates the large text inputs used by some benchmarks.
- `fasta.python3-3.py` - input generator used by `gen-input.sh`.
- `results/` - checked-in benchmark tables used for analysis.
- `archive/` - legacy planning notes kept for project history.

## Results layout

- `results/raw/` - direct outputs from benchmark runs when they are kept in this project.
- `results/summary/` - curated input tables such as `data.csv`.
- `results/derived/` - normalized or ratio tables produced from the summary data.

## Notes

- The large text benchmark inputs are generated in this folder because existing Makefiles reference them from here.
- Historical CSV files are kept because they support paper writing and later cross-checking.
- This folder is still active, but some outputs are historical snapshots rather than regularly refreshed data.
