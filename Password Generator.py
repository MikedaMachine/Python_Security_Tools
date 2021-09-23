import random

# values that can be used in any password
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
numbers = "0123456789"
symbols = "!@#$%^&*?_."

# Boolean expression to select true or false values
upper, lower, nums, syms = True, True, True, True

# contains all values used for a password
all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += numbers
if syms:
    all += symbols

# length of a password
length = 12

# the amount of passwords to be generated
amount_passwords = 5

# password function
for x in range (amount_passwords):
    password = "".join(random.sample(all,length))
    print(password)

