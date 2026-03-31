# find_substr.sh

## Description

A bash script that searches for a specific substring or search term within files, with support for filtering by filename
patterns or whole path patterns.

## Usage

```bash
./find_substr.sh [-f filename_pattern] [-w wholename_pattern] <search_term> [search_path]
```

## Options

- `-f filename_pattern`: Search only in files matching the specified filename pattern (e.g., `*.ini`, `file.txt`)
- `-w wholename_pattern`: Search only in files matching the specified whole path pattern (e.g., `*folder/*`,
  `*folder/file.txt`)
- `<search_term>`: (Required) The text to search for
- `[search_path]`: (Optional) The directory to start searching from. Defaults to current directory (`.`)

## Requirements

- Bash shell

## Examples

- Find by file type: `./find_substr.sh -f '*.ini' 'search string' .`
- Find by filename: `./find_substr.sh -f 'file.txt' 'search string' .`
- Find in subfolder: `./find_substr.sh -w '*folder/*' 'search string' .`
- Find in subfolder by name: `./find_substr.sh -w '*folder/file.txt' 'search string' .`

## Output

Displays a progress bar showing search progress and lists all files containing the search term with their absolute
paths.
