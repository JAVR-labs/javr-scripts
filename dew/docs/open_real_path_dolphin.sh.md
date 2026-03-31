# open_real_path_dolphin.sh

## Description

A bash script that opens a folder in the KDE Dolphin file manager, resolving symlinks to their real paths.

## Usage

> [!TIP]
> If you are going to use this script I recommend doing so through "_Open Folder With_" context menu instead of
> terminal.

```bash
./open_real_path_dolphin.sh <path>
```

- `<path>`: The path to the folder to open (can be a symlink)

## Functionality

1. Takes the provided path as input
2. Resolves any symlinks to their real path using `readlink -f`
3. Opens the resolved path in a new Dolphin window
4. Runs in the background without blocking the terminal

## Requirements

- KDE Dolphin file manager installed
- `readlink` command available (standard on Linux systems)

## Notes

- The script runs Dolphin detached (`nohup`) so it continues running even after the terminal closes
- Standard output and error output are redirected to `/dev/null`


