Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

# # Normal List :
word_len = []
for _ in Names :
    word_len.append(len(_))

print(word_len)

#List Comrehension :

word_len1 = [len(_) for _ in Names ]
print(word_len1)

#Functional Programming :

def word_length (x):
    return len(x)

word_len2 = map(word_length,Names)
print(list(word_len2))
