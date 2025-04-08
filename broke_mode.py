import os

BUDGET_FILE = "data/budget.txt"

def activate_broke_mode():
    """Activates broke mode by setting the minimum daily expense limit."""
    try:
        with open(BUDGET_FILE, "r") as file:
            lines = file.readlines()
        
        budget = float(lines[0].split(":")[1].strip())  # Total Budget
        expense_limit = float(lines[1].split(":")[1].strip())  # Allowed expense limit

        # Set new broke mode limit (minimum daily expense)
        new_limit = expense_limit * 0.6  # Reduce limit to 60% of current allowed expense
        
        # Update budget file
        with open(BUDGET_FILE, "w") as file:
            file.write(f"Budget: {budget}\n")
            file.write(f"Expense Limit: {new_limit}\n")

        print("\n🚨 BROKE MODE ACTIVATED 🚨")
        print(f"💰 New daily expense limit: ₹{new_limit:.2f}")
        print("Spend only on essential items!\n")

    except FileNotFoundError:
        print("❌ Budget not set. Run budget_plan.py first.")

if __name__ == "__main__":
    activate_broke_mode()
