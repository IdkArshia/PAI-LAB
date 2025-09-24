num = input("Enter a 4-digit number: ")
swapped=num[3]+num[2]+num[1]+num[0]
encrypted = ""
for d in swapped:
    encrypted += str((int(d) + 7) % 10)
print("Encrypted number:", encrypted)
