
# Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can be divided on x,y

def divided_numbers (x,y) :
    for n in range (1,101):
        if n%x == 0 and n%y == 0 :
            print(n)

first_number = int(input('Enter First Number : '))
second_number = int(input('Enter Second Number : '))

divided_numbers(first_number,second_number)
