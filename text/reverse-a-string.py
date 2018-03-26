def reverse(string):
    rev = []
    for i in range(len(string)):
        rev.append(string[i])
    rev = rev[::-1]
    return ''.join(str(x) for x in rev)  



string = input("Enter a string: ")
print(reverse(string))
