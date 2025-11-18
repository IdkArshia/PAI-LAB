try:
    name=input("Name: ")
    cnic=input("CNIC: ")
    age=input("Age: ")
    salary=input("Salary: ")

    with open("emp.txt","w") as f:
        f.write(name+"\n"+cnic+"\n"+age+"\n"+salary+"\n")

    contact=input("Contact number: ")

    with open("emp.txt","a") as f:
        f.write(contact+"\n")

    with open("emp.txt","r") as f:
        print(f.read())

except Exception as e:
    print("Error:",e)
