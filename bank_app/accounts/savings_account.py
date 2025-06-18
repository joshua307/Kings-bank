class SavingsAccount:
    def __init__(self, balance=0, limit=50000):
        self.balance = balance
        self.limit = limit

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ₦{amount} to Savings."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        if amount > self.limit:
            return f"Cannot withdraw more than ₦{self.limit} at once."
        self.balance -= amount
        return f"Withdrew ₦{amount} from Savings."

    def get_balance(self):
        return self.balance
