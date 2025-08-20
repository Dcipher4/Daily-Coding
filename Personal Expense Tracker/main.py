import csv
import os
from datetime import datetime

# Global Variables
expenses = []
monthly_budget = 0
datafile = "expenses.csv"
budget_file = "budget.txt"


def add_expense():
    """ Adding a new expense to the expense list """
    print("\n--- Add New Expense ---")

    while True:
        date = input("Enter date (DD-MM-YYYY): ")
        try:
            date_object = datetime.strptime(date, "%d-%m-%Y")
            formatted_date = date_object.strftime("%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

    category = input("Enter category of expense: ").strip().title()
    if not category:
        print("Invalid category. Category cannot be empty.")
        return

    while True:
        try:
            amount = float(input("Enter amount of expense: "))
            if amount <= 0:
                print("Invalid amount. Amount cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid amount. Amount cannot be empty.")

    description = input("Enter description of expense: ").strip()

    expense = {'date': formatted_date,
               'category': category,
               'amount': amount,
               'description': description}
    expenses.append(expense)
    print("Expense added successfully.")


def view_expenses():
    """ View all expenses """
    print("\n--- View All Expenses ---")

    if not expenses:
        print("No expenses were added.")
        return

    print_expenses_with_index()


def print_expenses_with_index():
    """Helper function to print expenses with index numbers"""
    total = 0
    print(f"{'Index':<6} | {'Date':<12} | {'Category':<15} | {'Amount':<10} | Description")
    print('-' * 70)

    for index, expense in enumerate(expenses, start=1):
        try:
            date = expense['date']
            category = expense['category']
            amount = float(expense['amount'])
            description = expense['description']

            if not all([date, category, description]):
                print(f"Skipping incomplete expense: {expense}")
                continue

            print(f"{index:<6} | {date:<12} | {category:<15} | Rs{amount:<9.2f} | {description}")
            total += amount
        except (KeyError, TypeError) as e:
            print(f"Skipping incomplete expense: {expense} ({str(e)})")

    print("-" * 70)
    print(f"Total expenses: Rs{total:.2f}\n")


def delete_expense():
    """Delete an expense from the list"""
    print("\n--- Delete Expense ---")

    if not expenses:
        print("No expenses to delete.")
        return

    print_expenses_with_index()

    while True:
        try:
            choice = input("Enter the index number of expense to delete (0 to cancel): ")
            if choice == '0':
                print("Deletion cancelled.")
                return

            index = int(choice) - 1
            if 0 <= index < len(expenses):
                deleted_expense = expenses.pop(index)
                print(
                    f"Deleted expense: {deleted_expense['date']} - {deleted_expense['category']} - Rs{deleted_expense['amount']}")
                save_expenses()  # Save changes immediately
                break
            else:
                print("Invalid index. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def set_budget():
    '''Monthly Budget'''
    global monthly_budget

    print("\n--- Set Budget ---")
    while True:
        try:
            budget = float(input("Enter budget: Rs"))
            if budget <= 0:
                print("Invalid budget. budget cannot be negative.")
                continue
            monthly_budget = budget
            save_budget()
            print(f"Monthly budget: Rs{monthly_budget:.2f}")
            break
        except ValueError:
            print("Invalid budget. budget cannot be empty.")


def track_budget():
    """Compare expenses against budget for a specific month"""
    print("\n--- Track Budget ---")

    if monthly_budget <= 0:
        print("Monthly budget not set. Please set your budget.")
        set_budget()
        return

    # Ask user for which month to track
    while True:
        month_year = input("Enter the month and year to track (MM-YYYY): ")
        try:
            # Parse the input to get month and year
            track_date = datetime.strptime(month_year, "%m-%Y")
            break
        except ValueError:
            print("Invalid format. Please use MM-YYYY format (e.g., 04-2023).")

    total_expenses = 0.0
    month_expenses = []

    # Calculate expenses for the specific month
    for expense in expenses:
        try:
            # Parse expense date string to datetime object
            expense_date = datetime.strptime(expense['date'], "%d-%m-%Y")

            # Check if expense is in the selected month/year
            if expense_date.month == track_date.month and expense_date.year == track_date.year:
                amount = float(expense['amount'])
                total_expenses += amount
                month_expenses.append(expense)
        except (KeyError, ValueError) as e:
            print(f"Skipping invalid expense record: {expense} ({str(e)})")
            continue

    remaining = monthly_budget - total_expenses

    # Display results
    print(f"\n--- Budget Summary for {month_year} ---")
    print(f"Monthly Budget: Rs{monthly_budget:.2f}")
    print(f"Total expenses for {month_year}: Rs{total_expenses:.2f}")

    if total_expenses > monthly_budget:
        print(f"\nWARNING: You have exceeded your budget by Rs{abs(remaining):.2f}!")
    else:
        print(f"\nYou have Rs{remaining:.2f} left in your budget for this month.")

    # Show expenses for the month
    if month_expenses:
        print("\nExpenses for this month:")
        print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | Description")
        print('-' * 60)
        for expense in month_expenses:
            print(
                f"{expense['date']:<12} | {expense['category']:<15} | Rs{float(expense['amount']):<9.2f} | {expense['description']}")
    else:
        print("\nNo expenses recorded for this month.")


def save_expenses():
    '''save expenses to a CSV'''
    try:
        with open(datafile, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
            writer.writeheader()
            writer.writerows(expenses)
        print(f"Expense saved to {datafile}")
    except Exception as e:
        print(f"Error saving expenses: {str(e)}")


def load_expenses():
    ''' Load Expenses from CSV file'''
    global expenses

    if not os.path.exists(datafile):
        return

    try:
        with open(datafile, mode='r') as file:
            reader = csv.DictReader(file)
            expenses = [row for row in reader]
        print(f"Expenses loaded from {datafile}")
    except Exception as e:
        print(f"Error loading expenses: {str(e)}")


def save_budget():
    ''' Save budget to file '''
    try:
        with open(budget_file, mode='w') as file:
            file.write(str(monthly_budget))
        print(f"Budget saved to {budget_file}")
    except Exception as e:
        print(f"Error saving budget: {str(e)}")


def load_budget():
    ''' Load budget from CSV file  '''
    global monthly_budget

    if not os.path.exists(budget_file):
        return

    try:
        with open(budget_file, mode='r') as file:
            monthly_budget = float(file.read())
        print(f"Budget loaded from: {budget_file}")
    except Exception as e:
        print(f"Error loading budget: {str(e)}")


def show_menu():
    '''Show menu'''
    print("\n=== Personal Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Set Monthly Budget")
    print("5. Track Monthly Budget")
    print("6. Save Expenses")
    print("7. Quit")


def main():
    '''Main function'''
    load_expenses()
    load_budget()

    while True:
        show_menu()
        choice = input("Enter your choice(1-7): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            set_budget()
        elif choice == '5':
            track_budget()
        elif choice == '6':
            save_expenses()
        elif choice == '7':
            print("Thank you for using Personal Expense Tracker. \n Saving data before exiting...")
            save_expenses()
            save_budget()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()