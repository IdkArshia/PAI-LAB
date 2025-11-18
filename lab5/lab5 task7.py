def fix_file():
    try:
        filename="replacement_needed.txt"
        with open(filename,'r') as f:
            txt=f.read()

        wrong=input("Wrong letter: ")
        correct=input("Correct letter: ")

        new_txt=""
        for ch in txt:
            if ch==wrong:
                new_txt+=correct
            else:
                new_txt+=ch

        with open(filename,'w') as f:
            f.write(new_txt)

        print("Fixed")
    except Exception as e:
        print("Error:",e)

fix_file()
