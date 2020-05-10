n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

if n1 > 0 and n2 > 0:
    div = n1 / n2 
    mult = n1 * n2
    sum = n1 + n2
    sub = n1 - n2

    print (f'Division: {div}, multiplication: {mult}, sum: {sum}, subsctraction: {sub}')

else:
    print ("Both numbers should be positive")