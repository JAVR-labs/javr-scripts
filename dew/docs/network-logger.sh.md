# network-logger.sh

## Description

A bash script that continuously pings a network address and logs results with timestamps to a file.

## Usage

```bash
./network-logger.sh [ip_address]
```

- `[ip_address]`: (Optional) IP address or hostname to ping. If not provided, the script will prompt for it
  interactively.

## Output

- Logs are saved to `./network-log` file
- Console output shows:
    - Green colored messages for successful pings
    - Yellow colored messages for unknown errors
    - Standard output for other conditions (unreachable, timeout, etc.)
- Each log entry includes a timestamp in `YYYY-MM-DD HH:MM:SS` format

## Requirements

- Bash shell

## Features

- Detects various network conditions:
    - Successful ping responses
    - Destination unreachable
    - Network unreachable
    - No route to host
    - Timeouts
    - Unknown host
    - DNS resolution failures
    - Packet filtering
- Colour-coded console output for different statuses
- Continuous logging with 1-second interval between pings

## Notes

- Creates or appends to `./network-log` file
- Runs indefinitely until manually stopped (Ctrl+C)
- Uses standard `ping` command with `-c1` flag (1 packet per iteration)
- Color codes are ANSI standard


