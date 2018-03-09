m = int(input("Digite m sendo positivo: "))
n = int(input("Digite n sendo positivo: "))
maior = 0
total = 0
a=0
b=0
for x in range(m+1):
    for y in range(n+1):       
        total = ((x*y) - (x**2) + y)
    if total > maior:
        maior = total
        a=x
        b=y
print("Máximo:",maior)
print("Par:",a,"e",b)
