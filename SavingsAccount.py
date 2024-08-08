from BankAccount import BankAccount

class SavingsAccount(BankAccount):

    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.set_balance(self.get_balance() + interest)
        print(f"${round(interest, 2)} was added to your account!")
        print(f"Your new balance is : {round(self.get_balance(), 2)}")


# Create an instance (object) of a savings account and test
david = SavingsAccount('David Blurton', 234000, .08)
print(david.get_balance())
david.add_interest()
david.add_interest()
david.add_interest()
david.add_interest()
david.add_interest()
david.add_interest()
david.add_interest()
