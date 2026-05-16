# ErlangServer

This folder contains the echo server case study used to compare Erlang, Java, and C under the same measurement workflow.
It mixes small source files, client drivers, and checked-in experiment outputs.

## Main contents

- `echo_*.erl`, `server*.erl`, `server*.c`, `*.java` - source files for the case study variants.
- `client_erlang_*.py` - measurement drivers for different Erlang client loads and platforms.
- `run_script.py` - simple orchestration script for sequential measurements.
- `norm.py` and `ratio.py` - analysis helpers for checked-in CSV data.
- `results/` - raw, summary, and derived experiment outputs.
- `archive/` - historical measurement copies and working notes.

## Results layout

- `results/raw/` - direct outputs produced by the measurement drivers.
- `results/summary/` - combined tables used as analysis inputs.
- `results/derived/` - ratio and normalized tables.

## Notes

- Most historical measurements in this case study were collected on Windows with Scaphandre and the Windows RAPL driver.
- Temporary JSON and text dumps now belong in `generated/` and are ignored by Git.
- The folder is still useful for reproducibility, but some files are clearly legacy and are now grouped under `archive/`.
