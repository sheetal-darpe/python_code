# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     print("Age is valid.")

# try:
#     check_age(-5)
# except ValueError as e:
#     print(f"Caught an exception: {e}")

class InsufficientFundsError(Exception):
    "Raised when a transaction exceeds the account balance."
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Withdrawal amount exceeds available balance.")
    return balance - amount

try:
    new_balance = withdraw(50, 100)
except InsufficientFundsError as e:
    print(f"Error: {e}")