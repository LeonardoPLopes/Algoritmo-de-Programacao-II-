'''def fatorial(num):
    fat=1
    for i in range (num, 1, -1):
        fat = fat * i
    return fat
num=int(input("Numero: "))
print(fatorial(num))'''

def fatorial(num):
    if num == 0 or num ==1:
        return 1
    else:
        return num fatorial( num - 1)
n = int(input("numero : "))
print(fatorial(num))



