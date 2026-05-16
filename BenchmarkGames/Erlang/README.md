# BenchmarkGames/Erlang

Status: **active benchmark set**.

## Purpose

This folder contains Erlang benchmark-game cases and aggregate outputs used to compare OTP/runtime behavior.

## Important files

- `compile_all.py` - iterates benchmark subfolders and triggers Makefile actions.
- `fannkuch-redux/`, `mandelbrot/`, `n-body/`, `reverse-complement/` - benchmark definitions and run parameters.
- `*.csv` at this level - aggregate outputs and OTP comparison data.

## Generated vs manual

- `.hipe` files and benchmark definitions are source inputs.
- `.json` measurement files and CSV outputs are generated from benchmark runs.

## Reproducibility

Keep benchmark inputs/definitions and published CSV outputs unchanged. If new benchmark outputs are produced, store them with clear names and context.
