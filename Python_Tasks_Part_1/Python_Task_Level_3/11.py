
fahrenheit = float(input('Enter Fahrenheit Temperature : '))

def fah_to_cer (x) :
    celsius = (x - 32) * 5/9
    print(f"{x} in Fahrenheit is equal to {celsius} in Celsius")

fah_to_cer(fahrenheit)