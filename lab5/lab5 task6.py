def save_question():
    try:
        s=input("Enter sentence: ")
        if s.endswith("?"):
            with open("questions.txt","w") as f:
                f.write(s)
            print("Saved")
        else:
            print("Not a question")
    except Exception as e:
        print("Error:",e)

save_question()
