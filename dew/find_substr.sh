#!/bin/bash

# --------------------------
# Default values
# --------------------------

filename_pattern=""
search_term=""
search_path="."


# --------------------------
# Functions
# --------------------------

ui_print() {
    if [ -t 1 ]; then
        echo "$*" >&2
    fi
}

count_files(){
    ui_print "Counting files..."

    total=$(find "${find_args[@]}" | wc -l)

    if [ -n "$filename_pattern" ]; then
        ui_print "Searching $total files matching '$filename_pattern' for: $search_term"
    else
        ui_print "Searching $total files for: $search_term"
    fi

    count=0
    matches=0
    found_files=()

    ui_print ""
}

search_files(){
    while IFS= read -r -d '' file; do
        count=$((count + 1))

        if grep -Fq "$search_term" "$file" 2>/dev/null; then
            matches=$((matches + 1))
            found_files+=("$(realpath "$file")")
        fi

        percent=$((count * 100 / total))
        printf "\r[%3d%%] %d/%d files | Matches: %d" "$percent" "$count" "$total" "$matches"
    done < <(find "${find_args[@]}" -print0)

    ui_print ""
    ui_print ""
    ui_print "Search complete! Found in $matches files:"
    ui_print ""
}


# --------------------------------------
# Options
# --------------------------------------

# Separate options from positional args
while getopts "f:w:" opt; do
    case $opt in
        f)
            filename_pattern="$OPTARG"
            ;;
        w)
            wholename_pattern="$OPTARG"
            ;;
    esac
done

# Shift to positional arguments
shift $((OPTIND -1))

# Set positional arguments
search_term="$1"
search_path="${2:-.}"

if [ -z "$search_term" ]; then
    ui_print "Usage: $0 [-f filename_pattern] [-w wholename_pattern] <search_term> [search_path]"
    ui_print ""
    ui_print "Examples:"
    ui_print "Find by type: $0 -f '*.ini' 'search string' ."
    ui_print "Find by name: $0 -f 'file.txt' 'search string' ."
    ui_print "Find in subfolder: $0 -w '*folder/*' 'search string' ."
    ui_print "Find in subfolder by name: $0 -w '*folder/file.txt' 'search string' ."
    exit 1
fi

# Build find arguments
find_args=("$search_path" -type f)
if [ -n "$filename_pattern" ]; then
    find_args+=(-name "$filename_pattern")
fi
if [ -n "$wholename_pattern" ]; then
    find_args+=(-wholename "$wholename_pattern")
fi

# --------------------------
# Main
# --------------------------

count_files
search_files

if [ ${#found_files[@]} -gt 0 ]; then
    for file in "${found_files[@]}"; do
        echo "  $file"
    done
else
    ui_print "  No matches found."
fi
