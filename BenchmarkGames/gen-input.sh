#!/bin/bash
set -euo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
FASTA_SCRIPT="$SCRIPT_DIR/fasta.python3-3.py"
KN_TMP="$SCRIPT_DIR/knucleotide-input25000000.txt.tmp"
REV_TMP="$SCRIPT_DIR/revcomp-input25000000.txt.tmp"
REG_TMP="$SCRIPT_DIR/regexredux-input5000000.txt.tmp"

cleanup() {
  rm -f "$KN_TMP" "$REV_TMP" "$REG_TMP"
}

trap cleanup EXIT INT TERM

if [[ ! -f "$FASTA_SCRIPT" ]]; then
  echo "Missing generator script: $FASTA_SCRIPT" >&2
  exit 1
fi

echo "Generating input for k-nucleotide benchmark"
python "$FASTA_SCRIPT" 25000000 > "$KN_TMP"
mv "$KN_TMP" "$SCRIPT_DIR/knucleotide-input25000000.txt"

echo "Generating input for reverse-complement benchmark"
python "$FASTA_SCRIPT" 25000000 > "$REV_TMP"
mv "$REV_TMP" "$SCRIPT_DIR/revcomp-input25000000.txt"

echo "Generating input for regex-redux benchmark"
python "$FASTA_SCRIPT" 5000000 > "$REG_TMP"
mv "$REG_TMP" "$SCRIPT_DIR/regexredux-input5000000.txt"
