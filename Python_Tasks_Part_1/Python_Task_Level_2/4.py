Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

# Normal List :
new_names =[]
for x in Names :
    if x.count('a') >=2 :
        new_names.append(x)

print(new_names)

#List Comrehension :

new_names1 = [x for x in Names if x.count('a')>=2 ]
print(new_names1)

#Functional Programming :

def count_a (x) :
    if x.count('a') >= 2 :
        return x
    
new_names2 = filter(count_a,Names)
print(list(new_names2))
