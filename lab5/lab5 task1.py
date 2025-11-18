try:
    filename=input("Enter filename: ")
    with open(filename,'r') as f:
        data=f.read()
        chars=len(data)
        words=len(data.split())
        print("Characters:",chars)
        print("Words:",words)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Error:",e)
