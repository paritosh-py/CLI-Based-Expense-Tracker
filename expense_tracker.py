import os
from datetime import datetime

STUDENT_FILE = "data/students.txt"
EXPENSES_FILE = "data/expenses.txt"
BUDGET_FILE = "data/budget.txt"

def load_student_profile():
    """Load student profile and return living type & expense categories."""
    if not os.path.exists(STUDENT_FILE):
        print("❌ No profile found. Please set up your profile first.")
        return None, None
    
    with open(STUDENT_FILE, "r") as file:
        lines = file.readlines()
    
    if len(lines) < 2:
        print("❌ Profile data is incomplete. Please set up your profile again.")
        return None, None
    
    living_type = lines[0].strip().split(": ")[1]
    categories = lines[1].strip().split(": ")[1].split(", ")
    
    return living_type, categories

def save_student_profile(living_type, categories):
    """Save updated student profile with new categories."""
    with open(STUDENT_FILE, "w") as file:
        file.write(f"LivingType: {living_type}\n")
        file.write("Expenses: " + ", ".join(categories) + "\n")

def load_budget():
    """Load the user's monthly budget and expense limit."""
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "r") as file:
            lines = file.readlines()

            budget = 0
            expense_limit = 0
            # Iterate over the lines to parse the values
            for line in lines:
                line = line.strip()
                if line.startswith("Budget:"):
                    budget = float(line.split(":")[1].strip())  # Extract the numeric value after "Budget:"
                elif line.startswith("Expense Limit:"):
                    expense_limit = float(line.split(":")[1].strip())  # Extract the numeric value after "Expense Limit:"

            print(f"🔍 Debug: Budget = {budget}, Expense Limit = {expense_limit}")

            return budget, expense_limit
    return 0, 0  # Return default 0 if no valid data




def log_expense():
    """Log an expense by asking the user for amount and category."""
    living_type, categories = load_student_profile()
    if not categories:
        print("❌ No expense categories available. Please set up your profile again.")
        return

    print("\n📌 Expense Categories:")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    amount = input("\nEnter amount spent: ").strip()
    if not amount.isdigit():
        print("❌ Invalid amount. Please enter a numeric value.")
        return

    category_input = input("Enter category number OR type a new category: ").strip()

    if category_input.isdigit():
        category_index = int(category_input) - 1
        if 0 <= category_index < len(categories):
            category = categories[category_index]
        else:
            print("❌ Invalid category selection.")
            return
    else:
        category = category_input
        if category not in categories:
            categories.append(category)
            save_student_profile(living_type, categories)  # Update profile with new category
            print(f"✅ New category '{category}' added!")

    date_str = datetime.now().strftime("%Y-%m-%d")
    with open(EXPENSES_FILE, "a") as file:
        file.write(f"{date_str}, {amount}, {category}\n")

    print(f"✅ Expense recorded: ₹{amount} for {category}")

def view_expenses():
    """Show today's expenses and available balance."""
    if not os.path.exists(EXPENSES_FILE):
        print("📂 No expenses recorded yet.")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    total_spent = 0
    expenses_today = []

    # Read expenses safely
    with open(EXPENSES_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            
            parts = line.split(", ")
            if len(parts) != 3:
                print(f"⚠️ Skipping malformed entry: {line}")
                continue  # Skip incorrectly formatted entries

            date, amount, category = parts
            if date == today:
                expenses_today.append((amount, category))
                total_spent += int(amount)

    # Load budget and expense limit
    budget, expense_limit = load_budget()
    available_balance = budget - total_spent if budget else "Not Set"

    print("\n📅 Expenses for Today:")
    if expenses_today:
        for amount, category in expenses_today:
            print(f"💰 ₹{amount} - {category}")
    else:
        print("🚫 No expenses recorded for today.")

    print(f"\n💳 Available Balance: ₹{available_balance}")
    print(f"💳 Expense Limit: ₹{expense_limit}")





if __name__ == "__main__":
    while True:
        print("\n📌 Main Menu:")
        print("1. Add Expense")
        print("2. Set Monthly Budget")
        print("3. View Today's Expenses & Balance")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            log_expense()
        elif choice == "2":
            budget = input("Enter your monthly budget: ").strip()
            if budget.isdigit():
                with open(BUDGET_FILE, "w") as file:
                    file.write(budget)
                print("✅ Budget saved!")
            else:
                print("❌ Invalid budget amount.")
        elif choice == "3":
            view_expenses()
        elif choice == "4":
            print("👋 Exiting... Have a great day!")
            break
        else:
            print("❌ Invalid choice. Try again.")
