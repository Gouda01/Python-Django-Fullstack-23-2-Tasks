email =input('Enter Your Email : ')

email_list = email.split('@')

user_name = email_list[0]
domain = email_list[1]

print(f'User name is : {user_name}')
print(f'The Domain is : {domain}')

# We can use other way witout make list :

user_name1 , domain1 = email.split('@')

print(f'User name is : {user_name1}')
print(f'The Domain is : {domain1}')

# By shearching i find We can use email.utils library too :

from email.utils import parseaddr

user_name2, domain2 = parseaddr(email)[1].split('@')

print(f'User name is : {user_name2}')
print(f'The Domain is : {domain2}')



