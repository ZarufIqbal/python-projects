import csv

file_name = "expenses.csv"


def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")

    file = open(file_name, "a", newline="")

    writer = csv.writer(file)
    writer.writerow([name, category, amount])

    file.close()

    print("Expense added successfully!")


def view_expenses():
    file = open(file_name, "r")

    reader = csv.reader(file)

    for row in reader:
        print(row)

    file.close()


def total_expense():
    total = 0

    file = open(file_name, "r")

    reader = csv.reader(file)

    next(reader)

    for row in reader:
        total += float(row[2])

    file.close()

    print("Total Expense:", total)


while True:

    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        break

    else:
        print("Invalid choice")
