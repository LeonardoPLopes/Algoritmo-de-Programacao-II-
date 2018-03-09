resultado=1
fatorial=int(input("Digite um fatorial inteiro: "))
if fatorial == 0 :
    print("O resutado é: 1")
else:
    for i in range(fatorial,0,-1):
        resultado=resultado*i
    print("O resultado é :",resultado)
    
