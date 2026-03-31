#!/bin/bash

# Resolve the real path of the selected folder (handles symlinks)
selected_path="$1"
real_path=$(readlink -f "$selected_path")

# Open a new Dolphin window at the resolved real path (detached, no console output)
nohup dolphin "$real_path" >/dev/null 2>&1 &
