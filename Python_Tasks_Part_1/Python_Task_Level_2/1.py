Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

# Normal Loop :
new_names = []
for x in Names :
    new_names.append(x.upper())
print (new_names)


#List Comrehension :
new_names1 = [x.upper() for x in Names]
print(new_names1)


#Functional Programming :
def upper_words (x) :
    return x.upper()
new_names2 = map(upper_words,Names)
print(list(new_names2))