expenses = {}

def add_expense(name, amount):
    expenses[name] = expenses.get(name, 0) + amount
    print(f"Added {amount} for {name}.")

def show_expenses():
    total = sum(expenses.values())
    print("Expenses:")
    for name, amount in expenses.items():
        print(f"{name}: {amount}")
    print(f"Total: {total}")

while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        n = input("Expense name: ")
        a = float(input("Amount: "))
        add_expense(n, a)
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")