import bcrypt
import getpass

password = input("Enter your password: ").encode()
try:
    rounds = int(input("️Enter cost factor (minimum recommended is 10): ").strip())
    if rounds < 10:
        print("Too low! Minimum recommended value is 10.")
        exit(1)
except ValueError:
    print("Invalid input. Please enter a number.")
    exit(1)
hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds))
print("\nBcrypt hash:\n" + hashed.decode())
