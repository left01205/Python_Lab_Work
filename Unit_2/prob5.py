class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account Number: {self.__account_number}, Balance: {self.__balance}"


# Creating an instance of BankAccount
account = BankAccount("1234567890", 1000)

# Accessing public methods
account.deposit(500)
account.withdraw(200)

# Will show error due to data hiding
# print(account.__balance)

# Accessing private attributes using getter method
print(account.get_balance())

# Accessing private attributes using __str__ method
print(account)