def palindrome(string):
    return string.lower() == string[::-1].lower()

inpt = input("Give string: ")
print(palindrome(inpt))
