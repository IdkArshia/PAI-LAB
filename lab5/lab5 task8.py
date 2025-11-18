try:
    a=int(input("Enter number 1: "))
    b=int(input("Enter number 2: "))
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid number")
except Exception as e:
    print("Error:",e)
