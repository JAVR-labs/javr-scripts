# Stalker_radio_track_rename.py

## Description

A Python script that manages and renames audio track files for the S.T.A.L.K.E.R. Anomaly custom radio mod. It ensures
that all track files in specified folders follow mod's naming convention.

## Usage

Put songs in mod's track folders and run the script. It will prompt you to add new paths if needed and will
automatically rename any non-conforming `.ogg` files to the correct format.

```bash
python3 Stalker_radio_track_rename.py
```

## Features

- Stores multiple track folder paths in `saved-paths.txt` for batch processing
- Automatically renames non-conforming `.ogg` files to the standard naming format
- Tracks naming convention: `track_<number>.ogg`
- Detects invalid tracks and renames them with incrementing numbers
- Interactive menu to add new paths

## Requirements

- Python 3.13

## Configuration

- Saved paths are stored in `saved-paths.txt` file (one path per line)
- Each path should be a directory containing `.ogg` files

## Workflow

1. Prompts user whether to add a new track folder path
2. If yes, adds the path to `saved-paths.txt` (skips if already exists)
3. Processes all saved paths:
    - Identifies `.ogg` files not following the `track_<number>.ogg` format
    - Renames them sequentially based on the highest existing track number
    - Prints count of renamed files per folder

## Output

- Console messages indicating paths added to configuration
- Summary of renamed tracks per folder

## Notes

- Extracts numeric values from filenames for sorting
- Requires read/write access to specified directories
- Preserves existing valid track files with the correct naming scheme


