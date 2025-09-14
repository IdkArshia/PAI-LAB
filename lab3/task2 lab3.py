def check(string):
  word=string[len(string)-1]
  if(word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u'):
    print("yes")
  else:
    print("No")
word=input("enter word")
check(word)