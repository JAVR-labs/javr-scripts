# Simple Stellaris Espionage Success Calculator CLI
# Formula: success % = max(10, min(90, 50 + (skill - difficulty) * 10))
# CLI with menu to set difficulty and skill, loops for changes
# Added cross-platform screen clearing for a clean "updating" UI feel

import os


def clear_screen():
    """Clear the terminal screen cross-platform."""
    os.system('cls' if os.name == 'nt' else 'clear')


def calculate_success(skill, difficulty):
    base = 50
    modifier = (skill - difficulty) * 10
    success = base + modifier
    success = max(10, min(90, success))  # Clamp between 10% and 90%
    return success


# Initialize default values
difficulty = 0
skill = 0

print("Stellaris Espionage Calculator CLI")
print("Enter numbers to set values, or 'q' to quit.")

while True:
    clear_screen()

    # Calculate and display current result
    chance = calculate_success(skill, difficulty)
    print("Current Settings:")
    print(f"1. Difficulty - {difficulty}")
    print(f"2. Skill bonus - {skill}")
    print(f"Result: {chance}%")

    # Menu prompt
    choice = input("\nChoose an option (1 for Difficulty, 2 for Skill bonus, q to quit): ").strip().lower()

    if choice == 'q':
        clear_screen()  # Optional: Clear on exit for cleanliness
        print("Exiting calculator.")
        break
    elif choice == '1':
        clear_screen()
        try:
            new_diff = int(input("Enter new Difficulty (integer): "))
            difficulty = new_diff
        except ValueError:
            input("Invalid input. Please enter an integer. Press Enter to continue.")
    elif choice == '2':
        clear_screen()
        try:
            new_skill = int(input("Enter new Skill bonus (integer): "))
            skill = new_skill
        except ValueError:
            input("Invalid input. Please enter an integer. Press Enter to continue.")
    else:
        input("Invalid choice. Please select 1, 2, or q. Press Enter to continue.")
