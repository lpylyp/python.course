dictA = {'Amazon' : 'South America',
         'Dnipro' : 'Europe',
         'Colorado' : 'North America'}



def summary(data):
    for key, value in data.items():
        print("The {} runs through {}.".format(key,value))

summary(dictA)


