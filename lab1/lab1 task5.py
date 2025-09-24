import random
name = input("Enter your name: ")
year = input("Enter your birth year: ")
first_three = ""
for c in name[:3]:
    first_three += random.choice([c.lower(), c.upper()])
last_two = year[-2:]
symbols = "@#%&*"
symbol = symbols[ord(name[0]) % len(symbols)]
password = first_three + last_two + symbol
print("Generated password:", password)
