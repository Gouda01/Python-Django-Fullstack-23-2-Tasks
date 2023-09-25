Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

# Normal List :
new_names = []
for x in Names :
    if 'a' in x :
        new_names.append(x)

print(new_names)

#List Comrehension :

new_names1 = [x for x in Names if 'a' in x]
print(new_names1)

#Functional Programming :
def filter_names (x) :
    if 'a' in x :
        return x
    
new_names2 = filter(filter_names,Names)
print(list(new_names2))

