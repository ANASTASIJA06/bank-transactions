# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# 


def deposit(transactions, amount):
    transactions.append(amount)
pass


def withdraw(transactions, amount):
     transactions.append(-amount)
pass
    

def check_balance(transactions):
    
    print("Balance is:", sum( transactions))

def list():
    print(transactions)

transactions = []


while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. List transactions")
    print("5. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = int(input("Enter amount: "))
        deposit(transactions,amount) 
    elif choice == '2':
        amount = int(input("Enter amount: "))
        withdraw(transactions, amount)
    elif choice == '3':
        check_balance(transactions)
    elif choice == '4':
        list()
    elif choice == '5':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
