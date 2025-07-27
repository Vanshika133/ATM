# atm_backend.py

class User:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = []

    # Function that adds the deposited amount to balance
    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited ₹{amount}")

    # Function to deduct withdrawn money from balance
    def withdraw(self, amount):
        if amount > self.balance:
            self.history.append(f"Failed withdrawal ₹{amount} (Insufficient funds)")
            return False
        self.balance -= amount
        self.history.append(f"Withdrew ₹{amount}")
        return True

    # Function to display last 5 transactions
    def get_history(self):
        return self.history[-5:]  # Last 5 transactions


# Dictionary to store details of registered users 
users_db = {
    "2468": User("Anisha", "2468", 5000),
    "5678": User("Ram", "5678", 3000)
}

# Function for authenticating the pin
def authenticate(pin):
    return users_db.get(pin)
