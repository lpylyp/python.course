e2g = {'stork' : 'storch',
       'hawk' : 'falke',
       'woodpecker' : 'specht',
       'owl' : 'eule'}

def find_word(dict, word):
    for key, value in dict.items():
        if str(key) == word:
            # print(str(key), + "in German would be ", + str(value))
            print("'{}' in German would be '{}'".format(key,value))

print(e2g)

find_word(e2g, 'owl')

e2g['Man'] = 'Mann'
e2g['Book'] = 'Buch'
print(e2g)


def get_list(dict):
    keylist = []
    valuelist = []
    for key, value in dict.items():

        keylist.append(key)
        valuelist.append(value)
    print(keylist)
    print(valuelist)

get_list(e2g)
