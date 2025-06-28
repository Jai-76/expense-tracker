class Expense:
    def __init__(self, date, description, amount):
        self.date = date  # Corrected from '-' to '='
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed successfully.")  # Corrected spelling
        else:
            print("Invalid expense index.")

    def view_expenses(self):
        if len(self.expenses) == 0:  # Corrected from 'self.expense' to 'self.expenses'
            print("No expense found.")
        else:
            print("Expense list:")
            for i, expense in enumerate(self.expenses, start=1):  # Corrected from 'self.expense' to 'self.expenses'
                print(f"{i}. Date: {expense.date}, Description: {expense.description}, Amount: ${expense.amount:.2f}")  # Corrected 'adte' to 'date'

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")  # Corrected 'view' to 'View'
        print("4. Total Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter the description: ")  # Corrected spacing
            amount = float(input("Enter the amount: "))
            expense = Expense(date, description, amount)
            tracker.add_expense(expense)
            print("Expense added successfully.")
        elif choice == "2":
            index = int(input("Enter the expense index to remove: ")) - 1
            tracker.remove_expense(index)
        elif choice == "3":
            tracker.view_expenses()
        elif choice == "4":
            tracker.total_expenses()  # Corrected from 'total_expense' to 'total_expenses'
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
