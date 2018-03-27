def piglatin(string):
    vowels = ['a','e','i','o','u','y']
    if string[0] in vowels:
        string = string + 'way'
    elif string[1] in vowels:
        cut = string[0:1]
        string = string[1::] + cut + 'ay'
    else:
        cut = string[0:2]
        string = string[2::] + cut + 'ay'

    return string

string = input('Give string: ')
print(piglatin(string))
