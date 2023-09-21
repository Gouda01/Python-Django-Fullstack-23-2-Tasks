
# Create a function that takes x,y and prints all the number that can be divide by y from x to 100

def divided_numbers (x,y) :
    for n in range (x,101):
        if n%y == 0 :
            print(n)

first_number = int(input('Enter First Number : '))
second_number = int(input('Enter Second Number : '))

divided_numbers(first_number,second_number)