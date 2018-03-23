
def inverted_index(str,files):
    found = []
    for k, file in files.items():
        if str in file:
            found.append(k)
    print(found)



#documents
files = {'d1': 'He likes to wink, he likes to drink.',
         'd2': 'He likes to drink, and drink, and drink.',
         'd3': 'The thing he likes to drink is ink.',
         'd4': 'The ink he likes to drink is pink.',
         'd5': 'He likes to wink and drink pink ink.'}

#inverted_index('he',files)
#inverted_index('drink',files)
#inverted_index('ink',files)
#inverted_index('likes',files)
#inverted_index('pink',files)
inverted_index('thing',files)
#inverted_index('wink',files)
