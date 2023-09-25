Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

# Normal Loop :
new_names = []
for x in Names :
    if x.startswith('t') :
        new_names.append(x)

print(new_names)

#List Comrehension :

new_names1 = [x for x in Names if x.startswith('t')]
print(new_names1)

#Functional Programming :

def start_word(x) :
    if x.startswith('t'):
        return x
    
new_names2 = filter(start_word,Names)
print(list(new_names2))
