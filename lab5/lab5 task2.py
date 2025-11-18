try:
    filename=input("Enter filename: ")
    find_word=input("Word to find: ")
    replace_word=input("Replace with: ")

    with open(filename,'r') as f:
        data=f.read()

    data=data.replace(find_word,replace_word)

    with open(filename,'w') as f:
        f.write(data)

    print("Replaced successfully")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Error:",e)
