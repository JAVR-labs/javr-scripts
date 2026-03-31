# EspionageCalc.py

## Description

A command-line calculator tool for determining espionage mission success chances in Stellaris.

## Usage

Open the tui:

```bash
python3 EspionageCalc.py
```

## Features

- Interactive menu-driven interface
- Cross-platform screen clearing (Windows and Unix-like systems)
- Real-time success chance calculation
- Loop for multiple calculations without restarting

## Requirements

- Python 3.13

## Output

Displays current settings and calculated success chance percentage.

## Formula

Success chance percentage = `max(10, min(90, 50 + (skill - difficulty) * 10))`

- Base success rate: 50%
- Modifier: (Skill - Difficulty) × 10
- Minimum success rate: 10%
- Maximum success rate: 90%
