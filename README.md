# SQAMIA_GREEN_JIT

This repository contains long-term research artifacts for energy and runtime benchmarking in Erlang-focused studies.

## Repository map

- `BenchmarkGames/` - Computer Language Benchmark Game based experiments and outputs.
- `ErlangServer/` - echo server case study (Erlang/C/Java comparison) and measurements.
- `RosettaQueens/` - Rosetta Code inspired OTP 23 vs OTP 26 experiments.
- `scripts/` - repository maintenance helpers.

## What is kept in version control

This repository intentionally keeps historical research outputs used in papers and reports:

- benchmark scripts and source files
- CSV outputs used in analysis
- measurement metadata and benchmark configurations
- legacy result folders needed for traceability

## Reproducibility and cleanup policy

- Do **not** delete historical outputs used in publications.
- New temporary outputs should be ignored by `.gitignore`.
- Use `scripts/cleanup_generated.sh` to remove local generated/cache files without touching tracked research artifacts.

## Folder documentation

Each major folder includes a README with:

- purpose and status (active/legacy)
- key scripts and outputs
- relation to the benchmark framework
- reproducibility notes
