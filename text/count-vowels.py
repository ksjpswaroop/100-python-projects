def count_vowels(string):
    vowels = {'a':0,'e':0,'i':0,'o':0,'u':0,'y':0}
    sumv = 0
    for i in range(0,len(string)):
        if string[i] in vowels.keys():
            vowels[string[i]]+=1
            sumv+=1
    print('Number of total vowels: ' + str(sumv))
    return vowels

string = input('Give string: ')
print(count_vowels(string))
