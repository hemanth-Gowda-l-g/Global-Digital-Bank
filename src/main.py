from services.banking_services import BankingService

def main():
    bank = BankingService()
    print("Welcome to GlobalDigital Bank")

    while True:
        print("\n--- Main Menu ---")
        print("1) Create Account")
        print("2) Deposit")
        print("3) Withdraw")
        print("4) Balance Inquiry")
        print("5) Close Account")
        print("6) Set PIN")
        print("7) Change PIN")
        print("8) Search Accounts")
        print("9) List All Accounts")
        print("10) View Transaction History")
        print("11) Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            age = input("Enter age: ")
            acc_type = input("Enter account type (Savings/Current): ")
            initial = input("Initial Deposit amount: ")
            set_pin = input("Set a 4-digit PIN? (y/n): ").strip().lower()
            pin = None
            if set_pin == "y":
                pin = input("Enter 4-digit PIN: ").strip()
            acc, msg = bank.create_account(name, age, acc_type, initial, pin=pin)
            print(msg)
            if acc:
                print(acc)

        elif choice == "2":
            acc_no = input("Enter account number: ")
            amount = input("Enter amount to deposit: ")
            ok, msg = bank.deposit(acc_no, amount)
            print(msg)

        elif choice == "3":
            acc_no = input("Enter your account number: ")
            amount = input("Enter amount to withdraw: ")
            pin = input("Enter PIN (press Enter if none): ").strip()
            ok, msg = bank.withdraw(acc_no, amount, pin=pin if pin else None)
            print(msg)

        elif choice == "4":
            acc_no = input("Enter Account Number: ")
            acc, msg = bank.balance_inquiry(acc_no)
            print(acc if acc else msg)

        elif choice == "5":
            acc_no = input("Enter account number to close: ")
            ok, msg = bank.close_account(acc_no)
            print(msg)

        elif choice == "6":
            acc_no = input("Enter account number: ")
            pin = input("Enter new 4-digit PIN: ").strip()
            ok, msg = bank.set_pin(acc_no, pin)
            print(msg)

        elif choice == "7":
            acc_no = input("Enter account number: ")
            old_pin = input("Enter current PIN: ").strip()
            new_pin = input("Enter new 4-digit PIN: ").strip()
            ok, msg = bank.change_pin(acc_no, old_pin, new_pin)
            print(msg)

        elif choice == "8":
            term = input("Enter search term (name, account number, type, or status): ")
            results = bank.search_accounts(term)
            if results:
                print(f"\nFound {len(results)} account(s):")
                for acc in results:
                    print(acc)
            else:
                print("No accounts found matching your search.")

        elif choice == "9":
            accounts = bank.list_accounts()
            if accounts:
                print(f"\nTotal accounts: {len(accounts)}")
                for acc in accounts:
                    print(acc)
            else:
                print("No accounts found.")

        elif choice == "10":
            acc_no = input("Enter account number (press Enter for all transactions): ").strip()
            transactions = bank.get_transaction_history(acc_no if acc_no else None)
            if transactions:
                print(f"\nTransaction History ({len(transactions)} record(s)):")
                for t in transactions:
                    print(t)
            else:
                print("No transactions found.")

        elif choice == "11":
            print("Thank you for visiting GlobalDigital Bank")
            break

        else:
            print("Invalid Choice.\n Try Again!!")

if __name__ == "__main__":
    main()

            