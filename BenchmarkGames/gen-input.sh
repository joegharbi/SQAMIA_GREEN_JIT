#!/bin/bash
set -euo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
FASTA_SCRIPT="$SCRIPT_DIR/fasta.python3-3.py"

if [[ ! -f "$FASTA_SCRIPT" ]]; then
  echo "Missing generator script: $FASTA_SCRIPT" >&2
  exit 1
fi

echo "Generating input for k-nucleotide benchmark"
python "$FASTA_SCRIPT" 25000000 > "$SCRIPT_DIR/knucleotide-input25000000.txt"

echo "Generating input for reverse-complement benchmark"
python "$FASTA_SCRIPT" 25000000 > "$SCRIPT_DIR/revcomp-input25000000.txt"

echo "Generating input for regex-redux benchmark"
python "$FASTA_SCRIPT" 5000000 > "$SCRIPT_DIR/regexredux-input5000000.txt"
