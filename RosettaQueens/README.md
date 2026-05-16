# RosettaQueens

Status: **active OTP comparison study**.

## Purpose

Contains Rosetta-style benchmark experiments (notably queens variants) used to compare OTP 23 vs OTP 26 for runtime/energy behavior.

## Important files

- `queens.erl`, `queens_list.erl`, `n_queens.erl` - benchmark implementations.
- `average.py` - aggregation helper for repeated measurements.
- `run_windows.py` - Windows orchestration helper.
- `*.csv` at this level - experiment outputs and aggregated comparison data.

## Legacy data

- `old_test/` contains older exploratory outputs kept for historical traceability.

## Reproducibility notes

- Main execution workflow is Windows-oriented.
- Keep existing historical CSV outputs used in publications/reports.
- Add new outputs with descriptive file names to preserve context.
