# print_file_contents.sh

## Description

A bash script that prints the contents of files matching a pattern, with support for directory exclusion. Made to make
it easy to send large quantities of small files to a language model.

## Usage

```bash
./print_file_contents.sh [-f <pattern>] [-e <exclude_dir>] [start_dir]
```

## Options

- `-h`: Display help message
- `-f <pattern>`: File pattern to match (default: `*`)
- `-e <exclude_dir>`: Directory path to exclude from search (e.g., `.venv`)
- `[start_dir]`: Starting directory for search (default: `.`)

## Requirements

- Bash shell

## Examples

- Print all Python files: `./print_file_contents.sh -f '*.py' .`
- Print all files excluding `.venv`: `./print_file_contents.sh -f '*.py' -e .venv .`
- Print all files in current directory: `./print_file_contents.sh`

## Output

Outputs files and their contents in a formatted structure:

~~~
=========================================
path/to/file1.txt:
```
contents of file1.txt
```

=========================================
path/to/file2.txt:
```
contents of file2.txt
```
~~~

## Notes

- File paths are separated by null characters to handle spaces and special characters
- Uses `find` with proper escaping for robust directory exclusion
- The exclude directory path is treated as relative to start_dir


