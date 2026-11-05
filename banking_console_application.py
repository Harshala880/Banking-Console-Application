# KIRAN ACADEMY - TASK 03
# BANKING CONSOLE APPLICATION

balance = 10000

print("Welcome to INDIA Bank")
print("Opening Balance: Rs.", balance)

while True:

    print("\n----- BANKING MENU -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Current Balance: Rs.", balance)

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Deposit successful.")
                print("Updated Balance: Rs.", balance)
            else:
                print("Invalid amount. Enter amount greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: "))

            if amount > 0:
                if amount <= balance:
                    balance -= amount
                    print("Withdrawal successful.")
                    print("Updated Balance: Rs.", balance)
                else:
                    print("Transaction failed: Insufficient balance.")
                    print("Current Balance: Rs.", balance)
            else:
                print("Invalid amount. Enter amount greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")