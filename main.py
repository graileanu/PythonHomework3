n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

if n1 > 0 and n2 > 0:
    div = n1 / n2 
    mult = n1 * n2
    print (f'Division result: {div}, multiplication result: {mult}')

else:
    print ("Both numbers should be positive")