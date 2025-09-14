def is_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False
word = input("Enter a string: ")
if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")
