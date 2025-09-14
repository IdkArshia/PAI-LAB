students= [("Ayesha",5),("sara",8),("Taha",9),("umer",3),("Laiba",10)]
n=len(students)
for i in range (n-1):
    for j in range(n-1-i):
        if(students[j][1]<students[j+1][1]):
            students[j], students[j + 1] = students[j + 1], students[j]
print("Top three students:\n")
for x in range(3):
    print(students[x])            