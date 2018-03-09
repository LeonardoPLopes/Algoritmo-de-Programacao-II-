'''def primo(num):
    c = 0
    for i in range(num, 0, -1):
        if n%i==0:
            c=c+1
    if c > 2:
        return False
    else:
        return True
num = int(input("Numero: "))
print(primo(num))'''

def primo(num, c, i):
    if i == 1:
        if c > 2:
            return False
        else:
            return True
    else:
        if num%i==0:
            c = c+1
        return primo(num, c, i-1)

c = 0
num = int(input("Numero: "))
i = num
print(primo(num, c, i))
