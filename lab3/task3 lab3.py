def employee(name, salary=10000):
  tax = salary * 0.02
  salary= salary - tax
  print(f"Employee Name: {name}")
  print(f"Salary after 2% tax: {salary}")

employee("Alice", 50000)
employee("Bob")
employee("Charlie", 75000.50)