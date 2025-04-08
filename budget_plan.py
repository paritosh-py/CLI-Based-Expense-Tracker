import os

BUDGET_FILE = "data/budget.txt"

def get_monthly_budget():
    """Ask user for their budget and provide savings plans every time they start the program."""
    print("\n💰 Budget Planning 💰")

    # Get budget input
    budget = float(input("\nEnter your monthly budget (₹): "))

    # Generate plans
    neutral_savings = budget * 0.8  # 80% for expenses
    high_savings = budget * 0.6  # 60% for expenses
    print("\n📊 Choose a savings plan:")
    print(f"1️⃣ Neutral Savings (₹{neutral_savings} for expenses)")
    print(f"2️⃣ Higher Savings (₹{high_savings} for expenses)")
    print("3️⃣ Custom Savings (You decide)")

    plan_choice = input("Enter 1, 2, or 3: ")

    if plan_choice == "1":
        selected_plan = neutral_savings
    elif plan_choice == "2":
        selected_plan = high_savings
    else:
        selected_plan = budget - float(input("How much do you want to save? (₹): "))

    # Save budget
    with open(BUDGET_FILE, "w") as file:
        file.write(f"Budget: {budget}\n")
        file.write(f"Expense Limit: {selected_plan}\n")

    print("✅ Budget and savings plan saved successfully!\n")
