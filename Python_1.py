import random
import datetime
from Quotes import display_quote, get_bonus_Tip, mood_based_motivation

# Student Productivity App
# This script provides a simple CLI with three main features:
# - Study planner: asks for subjects and returns a short schedule
# - To-do list: shows a few random chores to complete
# - Daily motivation: asks for the user's mood and returns a
#   mood-aligned quote, a small challenge, and a contextual bonus tip

# STUDY PLANNER

def study_planner():
    # Interactive study planner: collects subject names and returns a short schedule with recommended study hours.Hours are shortened for language/"soft-subjects".
    print("Welcome to your Study Planner!")
    subjects = []

    try:
        numbers = int(input("Enter the number of subjects you have: "))
    except ValueError:
        # If the user enters something that isn't an integer, inform them and return to the main menu.
        print("Please enter a valid number.")
        return

    for i in range(numbers):
        subject = input(f"Enter subject {i + 1}: ")
        subjects.append(subject.strip())

    if not subjects:
        # Nothing to schedule if the subject list is empty.
        print("No subjects entered.")
        return
    print()
    no_picked = min(3, len(subjects))
    chosen_subjects = random.sample(subjects, no_picked)

    print("Here's your study schedule for today:")
    for subject in chosen_subjects:
        if subject.lower() in ["life orientation", "isixhosa", "afrikaans", "english"]:
            hours = 2
        else:
            hours = 3
        # Print the suggested study time for each chosen subject.
        print(f"You should study {subject} for {hours} hours today.")


# TO-DO LIST

def to_do_list():
    # Simple list of household/study chores. We sample a few items each time the user opens the to-do list for variety.
    chores = [
        "Clean your room",
        "Take out the trash",
        "Clean your study area",
        "Help with cooking",
        "Sweep the floor",
    ]

    print("Today's Chores:")
    chores_today = random.sample(chores, 3)

    for i, chore in enumerate(chores_today, start=1):
        # Numbered output for readability
        print(f"{i} - {chore}")


# DAILY MOTIVATION

def motivation_generator():
    today = datetime.datetime.now()
    weekday = today.weekday()
    hour = today.hour
    # Ask the user for their current mood so we can provide a tailored quote and a short, achievable challenge.
    mood = input("How are you feeling today? (e.g., happy, sad, stressed, tired, anxious) : ").strip()

    # If the user doesn't enter a mood, do not proceed with feedback.
    if not mood:
        print("No mood entered. Returning to the main menu.")
        return

    # Get mood-based motivation (falls back to a random quote)
    quote, challenge, bonus_tip = mood_based_motivation(mood, weekday, hour)

    # Present the results clearly labeled so the user knows
    # which text is the quote and which is the suggested challenge.
    print("\nDaily Motivation:")
    print(f"Quote: {quote}")
    print(f"Challenge: {challenge}")
    print(bonus_tip)


# MAIN MENU

def main_menu():
    # Main interactive loop for the CLI menu. Keeps running until the user chooses to exit. Each numeric choice maps to a top-level feature implemented above.
    while True:
        print()
        print("STUDENT PRODUCTIVITY APP")
        print("1. Study Planner")
        print("2. To-Do List")
        print("3. Daily Motivation")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print()
            study_planner()
        elif choice == "2":
            print()
            to_do_list()
        elif choice == "3":
            print()
            motivation_generator()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            # Protect against invalid menu input and prompt again.
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()
