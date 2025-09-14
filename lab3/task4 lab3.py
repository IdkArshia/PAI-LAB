list1 = input("Enter first list (space separated): ").split()
list2 = input("Enter second list (space separated): ").split()
if len(list1) != len(list2):
    print("Both lists must have the same number of elements")
    exit()
dictionary = {}
for i in range(len(list1)):
    dictionary[list1[i]] = list2[i]
print(dictionary)
