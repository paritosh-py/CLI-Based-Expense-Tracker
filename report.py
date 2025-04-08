import os

BUDGET_FILE = "data/budget.txt"
EXPENSES_FILE = "data/expenses.txt"

def generate_report():
    """Generates an expense report showing total spending and remaining budget."""
    print("\n📊 EXPENSE REPORT 📊\n")

    try:
        with open(BUDGET_FILE, "r") as file:
            lines = file.readlines()
        
        total_budget = float(lines[0].split(":")[1].strip())  # Initial budget
        expense_limit = float(lines[1].split(":")[1].strip())  # Remaining budget

        total_spent = 0
        category_expenses = {}

        # Read and categorize expenses
        if os.path.exists(EXPENSES_FILE):
            with open(EXPENSES_FILE, "r") as file:
                expenses = file.readlines()

                for expense in expenses:
                    category, amount = expense.strip().split(": ₹")
                    amount = float(amount)
                    total_spent += amount

                    if category in category_expenses:
                        category_expenses[category] += amount
                    else:
                        category_expenses[category] = amount

        # Display report
        print(f"💰 Initial Budget: ₹{total_budget}")
        print(f"💸 Total Spent: ₹{total_spent}")
        print(f"📉 Remaining Budget: ₹{expense_limit}\n")

        print("📂 Expense Breakdown:")
        for category, amount in category_expenses.items():
            print(f"  - {category}: ₹{amount}")

        print("\n✅ Report generated successfully!")

    except FileNotFoundError:
        print("❌ Budget or expenses not found. Run budget_plan.py and expense_tracker.py first.")

if __name__ == "__main__":
    generate_report()
