# SQAMIA_GREEN_JIT

This repository collects three related research tracks around energy-aware benchmarking and Erlang runtime comparisons.
It is organized as a long-term research workspace, not as a single paper artifact.

## Repository map

- `BenchmarkGames/` - benchmark game case study and helper scripts for compiled benchmarks.
- `ErlangServer/` - echo server case study comparing Erlang, Java, and C.
- `RosettaQueens/` - Rosetta Code N-Queens study across OTP versions.

Each active project now follows the same layout when possible:

- `results/raw/` - direct measurement outputs kept for traceability.
- `results/summary/` - curated tables used as intermediate analysis inputs.
- `results/derived/` - normalized, averaged, or ratio outputs.
- `archive/` - legacy notes and historical material kept for context.
- `generated/` - temporary measurement dumps created during runs and ignored by Git.

## Reproducibility notes

Most historical measurement workflows were produced on Windows with Scaphandre and the Windows RAPL driver.
Some newer scripts also support Linux-based measurements.
Checked-in CSV files are intentionally kept because they are part of the research record and were used to compare framework iterations and paper results.

## Working with the repository

1. Read the README in the project you want to use.
2. Keep new raw outputs inside the matching `results/raw/` folder.
3. Keep temporary JSON or text dumps out of version control by writing them into `generated/`.
4. Move superseded experiments into `archive/` instead of deleting them when they still help explain published or historical results.
