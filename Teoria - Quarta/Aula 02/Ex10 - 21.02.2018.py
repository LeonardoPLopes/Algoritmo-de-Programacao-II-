def leEntrada():
    num=int(input("Digite um numero inteiro"))
    return num
def fibonacci(num):
    i=1
    a=0
    b=1
    while i <num:
        c=a+b
        print(c)
        a=b
        b=c
        i=i+1
    return b


fib=leEntrada()
print(fibonacci(fib))