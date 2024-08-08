
class BankAccount():

    def __init__(self, account_holder, balance = 0):
        self.__balance = balance # private attribute
        self.account_holder = account_holder

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, new_balance):
        self.__balance = new_balance

    # Getter
    def get_account_holder(self):
        return self.account_holder
    
    # Setter
    def set_account_holder(self, new_holder):
        self.account_holder = new_holder

    # Deposit method
    def deposit(self, amount):
        self.set_balance(self.get_balance() + amount)

    # Withdraw method
    def withdraw(self, amount):
        if 0 < amount and amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
        elif amount > self.get_balance():
            print("You don't have that much money in da bank!")
        else:
            print("Invalid entry. Enter a number greater than zero and less than your total balance")