
# Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in the x,y range


def odd_even_numbers (x,y) :
    
    odd_numbers = []
    even_numbers = []

    for n in range (x,y):
        if n%2 == 0 :
            odd_numbers.append(n)
        elif n%2 != 0 :           #We Can Use else: too
            even_numbers.append(n)
    
    print(f'Odd numbers between {x} and {y} is {odd_numbers}')
    print(f'Even numbers between {x} and {y} is {even_numbers}')

first_number = int(input('Enter First Number : '))
second_number = int(input('Enter Second Number : '))

odd_even_numbers(first_number,second_number+1)