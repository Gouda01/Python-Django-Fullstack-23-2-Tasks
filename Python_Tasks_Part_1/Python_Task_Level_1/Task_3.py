
# Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y

def multiplication_table (x,y) :
    
    # I use for and while loop for more learning And 2 run successefuly 
    
    for n in range(x,y+1):
        for m in range(1,13) :
            print(f'{x} * {m}\t= {x*m}')
            m += 1
        x += 1
        print('==============================================')

    '''
    
    while x <= y :
        m = 1
        while m <= 12 :
            print(f'{x} * {m}\t= {x*m}')
            m += 1
        x += 1
        print('==============================================')
    '''
    

first_number = int(input('Enter first number : '))
second_number = int(input('Enter second number : '))

multiplication_table(first_number,second_number)