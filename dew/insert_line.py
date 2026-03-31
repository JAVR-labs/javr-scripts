#!/usr/bin/env python3
from pathlib import Path

# ============ CONFIGURATION ============
SEARCH_LINE = 'IsEquippedRightHasKeyword("Smooth Weapon.esm" | 0x000806)'
INSERT_LINE = 'IsEquippedRightHasKeyword("Sonders_Keyword_Distribution.esp" | 0x00057D8E) OR'
INPUT_FILE = 'tmp'
CREATE_BACKUP = True


# =======================================

def insert_line_before(file_path, search_line, insert_line, backup=True):
    """Insert a line before the first occurrence of search_line in file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        modified = False
        new_lines = []

        for i, line in enumerate(lines):
            if not modified and line.strip() == search_line.strip():
                # Check if the previous line is already the insert line
                if i > 0 and lines[i - 1].strip() == insert_line.strip():
                    print(f"  → Already exists, skipping: {file_path}")
                    return None  # Special return value for "already exists"

                # Insert the new line before this one
                new_lines.append(insert_line if insert_line.endswith('\n') else insert_line + '\n')
                modified = True
            new_lines.append(line)

        if modified:
            if backup:
                backup_path = Path(str(file_path) + '.bak')
                backup_path.write_text(''.join(lines), encoding='utf-8')

            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)

            return True
        else:
            return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            file_paths = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Input file '{INPUT_FILE}' not found. Create it with one file path per line.")
        return
    except Exception as e:
        print(f"Error reading '{INPUT_FILE}': {e}")
        return

    if not file_paths:
        print("No file paths found in input file.")
        return

    files_to_process = [Path(path) for path in file_paths]

    print(f"Processing {len(files_to_process)} files from '{INPUT_FILE}'...")
    print(f"Searching for: {SEARCH_LINE}")
    print(f"Inserting: {INSERT_LINE}")
    print()

    modified_count = 0
    skipped_count = 0

    for file_path in files_to_process:
        if not file_path.is_file():
            print(f"⚠ Skipping {file_path}: not a file")
            continue

        result = insert_line_before(file_path, SEARCH_LINE, INSERT_LINE, backup=CREATE_BACKUP)

        if result is True:
            print(f"✓ Modified: {file_path}")
            modified_count += 1
        elif result is None:
            skipped_count += 1
        else:
            print(f"- No match: {file_path}")

    print()
    print(f"Complete! Modified {modified_count}/{len(files_to_process)} files.")
    if skipped_count > 0:
        print(f"Skipped {skipped_count} files (line already exists)")
    if CREATE_BACKUP and modified_count > 0:
        print("Backup files created with .bak extension")


if __name__ == '__main__':
    main()
