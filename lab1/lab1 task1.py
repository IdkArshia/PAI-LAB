num = input("Enter a number: ")
num_int = int(num)
num_float = float(num_int)
num_str = str(num_int)
num_complex = complex(num_int)
print("Original (int):", num_int)
print("Float:", num_float)
print("String:", num_str)
print("Complex:", num_complex)
if (num_int // 2) * 2 == num_int:
    print(f"{num_int} is divisible by 2")
else:
    print(f"{num_int} is not divisible by 2")
