# insert_line.py

## Description

A Python script that inserts a specified line of text before the first occurrence of a search line in multiple
files.<br>
Made specifically for mass modification of Skyrim's DAR/OAR conditions.

## Usage

```bash
python3 insert_line.py
```

The script reads file paths from a `tmp` file (one path per line) and processes each file.

## Configuration

Configure the following variables at the top of the script:

- `SEARCH_LINE`: The line to search for
- `INSERT_LINE`: The line to insert before the search line
- `INPUT_FILE`: The file containing list of file paths to process (default: `tmp`)
- `CREATE_BACKUP`: Whether to create backup files with `.bak` extension (default: `True`)

## Requirements

- Python 3.13

## Output

- Prints the status of each file processed
- Shows count of modified files, skipped files, and files with no matches
- Creates backup files if enabled

## Notes

- The script performs exact whitespace matching when comparing lines
- Will skip insertion if the line already exists immediately before the search line
- Backup files are created with `.bak` extension when modifications are made


