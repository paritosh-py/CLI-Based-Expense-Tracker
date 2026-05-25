# 💰 CLI-Based Expense Tracker

A command-line application designed specifically for students to track their daily expenses, manage budgets, and achieve savings goals. This tool helps students understand their spending patterns and make informed financial decisions.

## 📋 Features

### Core Functionality
- **📌 Expense Logging**: Record daily expenses with custom or predefined categories
- **💳 Balance Tracking**: View today's expenses and available balance at a glance
- **💰 Budget Planning**: Set monthly budgets with smart savings plan suggestions
- **🚨 Broke Mode**: Emergency feature to reduce spending limits when funds are running low
- **📊 Expense Reports**: Generate detailed breakdowns of spending by category
- **👤 Student Profiles**: Personalized setup based on living situation (Hosteler, Flat/PG, Day Scholar)

### Smart Categories
The application comes with pre-configured expense categories based on your living situation:
- **Hosteler**: Food, Academic
- **Flat/PG**: Rent, Groceries, Utilities, Academic
- **Day Scholar**: Traveling, Academic
- **Custom Categories**: Add your own categories on the fly

### Savings Plans
Choose from three budget allocation strategies:
1. **Neutral Savings**: 80% for expenses, 20% for savings
2. **Higher Savings**: 60% for expenses, 40% for savings
3. **Custom Savings**: Define your own savings target

## 🎯 How to Use

### Getting Started

1. **Run the main application**:
   ```bash
   python main.py
   ```

2. **Initial Setup**:
   - Select your living situation (Hosteler, Flat/PG, Day Scholar)
   - Enter your monthly budget (₹)
   - Choose a savings plan

### Main Menu Options

| Option | Description |
|--------|-------------|
| **1️⃣ Add Expense** | Log a new expense with amount and category |
| **2️⃣ View Expenses** | Display today's expenses and available balance |
| **3️⃣ Enable Broke Mode** | Reduce spending limit to 60% for essential expenses only |
| **4️⃣ Exit** | Close the program (all data is cleared) |

### Example Workflow

```
🏠 Student Profile Setup 🏠
Where do you live?
1️⃣ Hostel
2️⃣ Flat/PG
3️⃣ Day Scholar
Enter your choice: 1

💰 Budget Planning 💰
Enter your monthly budget (₹): 10000

📊 Choose a savings plan:
1️⃣ Neutral Savings (₹8000 for expenses)
2️⃣ Higher Savings (₹6000 for expenses)
3️⃣ Custom Savings (You decide)
Enter 1, 2, or 3: 1

✅ Budget and savings plan saved successfully!

📌 Main Menu
1️⃣ Add Expense
2️⃣ View Expenses
3️⃣ Enable Broke Mode
4️⃣ Exit (Deletes All Data)
```

## 📂 File Structure

```
CLI-Based-Expense-Tracker/
├── main.py              # Main application entry point
├── expense_tracker.py   # Core expense logging and viewing functions
├── budget_plan.py       # Budget planning and savings plan setup
├── report.py            # Generate expense reports
├── broke_mode.py        # Emergency spending limit reducer
├── student_profile.py   # Student profile management
├── data/               # Data directory (created at runtime)
│   ├── student_profile.txt
│   ├── budget.txt
│   ├── expenses.txt
│   └── students.txt
└── README.md
```

## 🔧 Core Modules

### `main.py`
- Entry point for the application
- Manages the main menu and navigation
- Handles student profile setup on each startup
- Data cleanup on exit

### `expense_tracker.py`
- **log_expense()**: Log a new expense with category
- **view_expenses()**: Display today's total spending and available balance
- Supports dynamic category creation
- Validates user inputs for data integrity

### `budget_plan.py`
- **get_monthly_budget()**: Set up monthly budget and savings plan
- Provides three preset savings strategies
- Calculates expense limits based on chosen plan

### `broke_mode.py`
- **activate_broke_mode()**: Reduces expense limit to 60% for emergency situations
- Encourages essential-only spending

### `student_profile.py`
- **get_user_profile()**: Collect student information and preferences
- Sets default expense categories based on living situation
- Allows custom category addition

### `report.py`
- **generate_report()**: Display comprehensive expense breakdown
- Shows total spending vs. budget
- Categorizes expenses for analysis

## 💡 Use Cases

- 🎓 **College Students**: Track hostel/PG expenses efficiently
- 👨‍🎓 **Budget-Conscious Students**: Set savings targets and monitor progress
- 💸 **Financial Discipline**: Build healthy spending habits
- 📊 **Spending Analysis**: Understand where money goes each month

## 💾 Data Storage

All data is stored in plain text files in the `data/` directory:
- **student_profile.txt**: Living situation and expense categories
- **budget.txt**: Monthly budget and expense limits
- **expenses.txt**: Daily expense logs (date, amount, category)
- **students.txt**: Student profile details

⚠️ **Note**: When you exit the program (Option 4), all saved data is permanently deleted to maintain privacy.

## 🚀 Key Features Explained

### Dynamic Categories
Add expenses to predefined categories or create new ones on-the-fly. The system automatically saves new categories to your profile.

### Real-time Balance Tracking
View available balance instantly based on today's spending against your budget.

### Broke Mode
When funds run low, activate "Broke Mode" to reduce your expense limit to 60%, encouraging essential-only spending.

### Privacy-First Design
All data is cleared when the program exits, ensuring your financial information isn't stored permanently on your device.

## 🛠️ Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## 🏃 Running the Application

```bash
# Start the program
python main.py
```

## 📝 Example Expense Log Entry

```
2025-04-08, 250, Food
2025-04-08, 150, Academic
2025-04-08, 100, Entertainment
```

## ✅ Best Practices

1. **Be Honest**: Record all expenses for accurate tracking
2. **Review Daily**: Check your balance regularly using Option 2
3. **Use Broke Mode**: When approaching your limit, activate it to prioritize essentials
4. **Choose Appropriate Plan**: Select a savings plan that matches your financial goals

## 🎓 Educational Purpose

This project is designed as a learning tool for students to:
- Develop financial literacy
- Practice budgeting skills
- Build disciplined spending habits
- Understand personal finances

---

**Created for students, by students. Stay financially aware! 💪**
