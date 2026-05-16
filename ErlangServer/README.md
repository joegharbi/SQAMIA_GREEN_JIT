# ErlangServer

Status: **active case study** with legacy outputs preserved.

## Purpose

Echo server benchmark case study comparing Erlang, C, and Java under different client and scheduling settings.

## Important scripts

- `measure_start.py` - CLI measurement driver around Scaphandre JSON output.
- `client_erlang_*.py` - workload launch variants.
- `norm.py`, `ration.py`, `consumption.py` - post-processing and aggregation helpers.

## Important outputs

- `*.csv` in this folder - processed and comparison outputs used in analysis.
- `old_measurements/` - legacy raw reports and historical exports.

## Generated vs manual

- Source files (`.erl`, `.c`, `.java`, `.py`) are manually maintained.
- Many CSVs are generated experiment outputs and kept for reproducibility.

## Reproducibility notes

- Workflow was primarily executed on Windows with Scaphandre and RAPL driver.
- Keep historical outputs that support reported findings.
- Use `../scripts/cleanup_generated.sh` for local cache/generated cleanup only.
