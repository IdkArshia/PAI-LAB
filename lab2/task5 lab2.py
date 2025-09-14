students={"Ayesha":5, "sara":6,"Taha":9,"Umer":8,"laiba":10}
highest=0
def add_student(name,marks):
    students[name]=marks
def update_marks(name, newM):
    students[name]=newM
def delete_students(name):
    del students[name]
def find_topper():
    highest = -1
    topper = None
    for name, marks in students.items():
        if marks > highest:
            highest = marks
            topper = name
    print(f"Topper: {topper} with {highest} marks")


add_student("Arshia",8)
update_marks("sara",7)
delete_students("Taha")
find_topper()
print(students)