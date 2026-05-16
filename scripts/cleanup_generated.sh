#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PATTERNS=(
  "__pycache__"
  "*.pyc"
  "*.pyo"
  "*.beam"
  "*.dump"
  "erl_crash.dump"
  "*.class"
  "*.tmp"
  "*.temp"
  "*.log"
)

DRY_RUN=true
if [[ "${1:-}" == "--apply" ]]; then
  DRY_RUN=false
fi

echo "Repository root: $ROOT_DIR"
echo "Mode: $([[ "$DRY_RUN" == true ]] && echo dry-run || echo apply)"

tmp_file="$(mktemp)"

for pattern in "${PATTERNS[@]}"; do
  find . -path './.git' -prune -o -type d -name "$pattern" -print >> "$tmp_file" || true
  find . -path './.git' -prune -o -type f -name "$pattern" -print >> "$tmp_file" || true
done

sort -u "$tmp_file" | while read -r path; do
  [[ -z "$path" ]] && continue
  if git ls-files --error-unmatch "$path" >/dev/null 2>&1; then
    continue
  fi

  if [[ "$DRY_RUN" == true ]]; then
    echo "Would remove: $path"
  else
    if [[ -d "$path" ]]; then
      rm -rf "$path"
    else
      rm -f "$path"
    fi
    echo "Removed: $path"
  fi
done

rm -f "$tmp_file"

echo "Done."
