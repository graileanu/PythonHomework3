n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

if n1 > 0 and n2 > 0:
    sum = n1 + n2 
    sub = n1 - n2
    print (f'Sum result: {sum}, substraction result: {sub}')

else:
    print ("Both numbers should be positive")