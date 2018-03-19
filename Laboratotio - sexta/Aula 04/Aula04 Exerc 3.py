def mdc(num1, num2):
    resto = None
    while resto is not 0:
        resto = num1 % num2
        num1  = num2
        num2  = resto

    return num1
num1 = int(input("N1:"))
num2 = int(input("N2:"))
print(mdc(num1, num2))

#Rec

def mdc(num1, num2):
    global resto
    resto = num1 % num2
    num1  = num2
    num2  = resto
    if resto is not 0:
        return (mdc(num1, num2))
    else:
        return num1

resto = None
num1 = int(input("N1:"))
num2 = int(input("N2:"))
print(mdc(num1, num2))
