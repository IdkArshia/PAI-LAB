try:
    l1=input("Enter first list elements separated by space: ").split()
    l2=input("Enter second list elements separated by space: ").split()

    if len(l1)!=len(l2):
        print("Lists must have same size")
    else:
        d={}
        for i in range(len(l1)):
            d[l1[i]]=l2[i]

        with open("dict.txt","w") as f:
            f.write(str(d))

        print("Dictionary saved")
except Exception as e:
    print("Error:",e)
