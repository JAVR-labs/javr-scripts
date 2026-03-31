# Keyboard_key_check.py

## Description

A Python diagnostic tool that detects and logs keyboard key press and release events in real-time.
Made for confirming and debugging keyboard malfunctions.

## Usage

```bash
python3 Keyboard_key_check.py
```

## Features

- Continuously listens for keyboard input
- Tracks all pressed and released keys
- Logs when keys are first pressed and when they are released
- Prints a separator line when all keys are released

## Requirements

- Python 3.13
- `keyboard` library (install with `pip install keyboard`)

## Output

Console output showing:

- "Pressed: <key_name>" - when a key is pressed
- "Released: <key_name>" - when a key is released
- "-------------------" - separator when all keys are released

## Exit Condition

Press the `End` key to stop the script.

## Notes

- Requires permissions to read keyboard input (may need to run with elevated privileges on some systems)
- Tracks keys by name in lowercase
- Maintains state for each key to avoid duplicate press/release messages


