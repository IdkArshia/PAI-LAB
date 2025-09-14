password = input("enter password: ")
letter = False
numbers = False
character = False
if len(password) < 8:
    print("password too short")
    exit()
for x in password:
    if (ord(x) > 64 and ord(x) < 91) or (ord(x) > 96 and ord(x) < 123):
        letter = True
    if ord(x) >= 48 and ord(x) <= 57:
        numbers = True
    if ord(x) == 64 or ord(x) == 35 or ord(x) == 36 or ord(x) == 37:
        character = True
if letter == True and numbers == True and character == True:
    print("password is valid")
else:
    print("invalid password")
