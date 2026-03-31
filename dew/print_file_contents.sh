#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage: script.sh [-f <pattern>] [-e <exclude_dir>] [start_dir]
Example: script.sh -f '*.py' -e .venv .
EOF
}

print_files() {
  local pattern="$1"
  local start_dir="$2"
  local exclude="$3"

  # 1. Remove trailing slash from exclude if it exists (crucial for find)
  exclude="${exclude%/}"

  # 2. Use \( \) for explicit logic grouping
  # If it matches the path, prune it.
  # OR (if it doesn't match), check if it's a file and print it.
  if [[ -n "$exclude" ]]; then
    find "$start_dir" \
      \( -path "$start_dir/$exclude" -prune \) \
      -o \( -type f -name "$pattern" -print0 \) | process_output
  else
    find "$start_dir" -type f -name "$pattern" -print0 | process_output
  fi
}

process_output() {
  while IFS= read -r -d '' file; do
    printf '%s\n' "========================================="
    printf '%s\n' "$file:"
    printf '%s\n' '```'
    cat -- "$file"
    printf '\n%s\n\n' '```'
  done
}

# --- Argument Parsing ---
if [[ $# -eq 0 ]]; then usage; exit 0; fi

pattern='*'
start_dir='.'
exclude_dir=''

parsed="$(getopt -o 'hf:e:' -- "$@")" || { usage; exit 2; }
eval set -- "$parsed"

while true; do
  case "$1" in
    -h) usage; exit 0 ;;
    -f) pattern="$2"; shift 2 ;;
    -e) exclude_dir="$2"; shift 2 ;;
    --) shift; break ;;
    *)  usage; exit 2 ;;
  esac
done

if [[ $# -ge 1 ]]; then start_dir="$1"; fi
if [[ ! -d "$start_dir" ]]; then
  printf 'Error: %s is not a directory\n' "$start_dir" >&2
  exit 2
fi

print_files "$pattern" "$start_dir" "$exclude_dir"
