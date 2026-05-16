# BenchmarkGames

Status: **active research area** with historical results kept for reproducibility.

## Purpose

This folder contains benchmark-game based experiments used to compare energy and runtime behavior, especially across OTP versions and language implementations.

## Main content

- `Erlang/` - Erlang benchmark cases, benchmark-specific Makefiles, and OTP comparison CSV outputs.
- `compile_all.py` - helper to run compile/run/measure actions across benchmark folders.
- `*.csv` at this level - consolidated/normalized outputs used in analysis.
- `old_measurements/` - legacy and historical measurement exports kept for traceability.

## Generated vs manual

- Benchmark source/configuration files are manually maintained.
- CSV outputs and some JSON measurement files are generated during experiments.
- Legacy generated outputs are intentionally versioned when tied to paper analysis.

## Reproducibility notes

- Existing files reflect a Windows-based measurement workflow.
- Keep historical CSV/JSON outputs unless they are clearly unrelated temporary files.
- For local cleanup of caches and bytecode-like artifacts, use `../scripts/cleanup_generated.sh`.
