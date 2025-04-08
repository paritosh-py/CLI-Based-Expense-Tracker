import os
import budget_plan  # Ensure budget_plan.py exists and has the necessary functions
import expense_tracker  # Ensure expense_tracker.py exists and has the necessary functions

STUDENT_PROFILE_FILE = "data/student_profile.txt"
BUDGET_FILE = "data/budget.txt"
EXPENSE_FILE = "data/expenses.txt"

def setup_student_profile():
    """Ask the student for their living situation every time the program starts."""
    print("\n🏠 Student Profile Setup 🏠")
    print("Where do you live?")
    print("1️⃣ Hostel")
    print("2️⃣ Flat/PG")
    print("3️⃣ Day Scholar")

    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        living_situation = "Hostel"
    elif choice == "2":
        living_situation = "Flat/PG"
    else:
        living_situation = "Day Scholar"

    # Save living situation
    with open(STUDENT_PROFILE_FILE, "w") as file:
        file.write(f"Living Situation: {living_situation}\n")

    print(f"✅ Your living situation '{living_situation}' has been saved!\n")

def reset_data():
    """Deletes all saved data when the program exits."""
    if os.path.exists(BUDGET_FILE):
        os.remove(BUDGET_FILE)
    if os.path.exists(EXPENSE_FILE):
        os.remove(EXPENSE_FILE)
    if os.path.exists(STUDENT_PROFILE_FILE):
        os.remove(STUDENT_PROFILE_FILE)

def main_menu():
    """Main menu to navigate the program."""
    setup_student_profile()  # Ask for living situation every time
    budget_plan.get_monthly_budget()  # Ask for new budget every time

    while True:
        print("\n📌 Main Menu")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Enable Broke Mode")
        print("4️⃣ Exit (Deletes All Data)")

        choice = input("Enter your choice: ")
        if choice == "1":
            expense_tracker.log_expense()
        elif choice == "2":
            expense_tracker.view_expenses()
        elif choice == "3":
            budget_plan.broke_mode()
        elif choice == "4":
            print("🔄 Deleting all data and exiting...")
            reset_data()  # Delete everything before exiting
            print("👋 All data cleared. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
