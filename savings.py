from account import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, interestRate, time):
        BankAccount.__init__(self)
        self.interest_rate = interestRate/100.0
        self.time = time

    def calculate_interest(self):
        self.balance *= self.interest_rate * self.time
        return self.balance
