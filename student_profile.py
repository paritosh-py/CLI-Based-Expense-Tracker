import os

STUDENT_FILE = "data/students.txt"

def get_user_profile():
    """Get user details and save them to a file."""
    print("\n🔹 Welcome to Personalized Expense Tracker 🔹")

    # Check if profile exists
    if os.path.exists(STUDENT_FILE) and os.path.getsize(STUDENT_FILE) > 0:
        print("✅ Profile already exists. Skipping setup.")
        return

    # Ask for living situation
    print("\nWhere do you live? Choose an option:")
    print("1. Hosteler\n2. Flat/PG\n3. Day Scholar")
    choice = input("Enter 1, 2, or 3: ")

    living_type = {
        "1": "Hosteler",
        "2": "Flat/PG",
        "3": "Day Scholar"
    }.get(choice, "Unknown")

    if living_type == "Unknown":
        print("❌ Invalid choice. Restarting setup...")
        return get_user_profile()

    # Default expenses based on living type
    default_expenses = {
        "Hosteler": ["Food", "Academic"],
        "Flat/PG": ["Rent", "Groceries", "Utilities", "Academic"],
        "Day Scholar": ["Traveling", "Academic"]
    }

    print("\n📌 Default expense categories for", living_type)
    print(", ".join(default_expenses[living_type]))

    # Allow user to add custom categories
    custom_categories = input("\nWant to add your own categories? (comma-separated, or press Enter to skip): ").strip()

    # Validate input: Only add categories if they are meaningful (not just a single digit)
    if custom_categories and not custom_categories.isdigit():
        custom_expenses = [x.strip() for x in custom_categories.split(",") if x.strip()]
    else:
        custom_expenses = []

    # Save profile
    with open(STUDENT_FILE, "w") as file:
        file.write(f"LivingType: {living_type}\n")
        file.write("Expenses: " + ", ".join(default_expenses[living_type] + custom_expenses) + "\n")
        file.flush()  # Ensures data is written immediately

    print("✅ Profile saved successfully!\n")

if __name__ == "__main__":
    get_user_profile()
