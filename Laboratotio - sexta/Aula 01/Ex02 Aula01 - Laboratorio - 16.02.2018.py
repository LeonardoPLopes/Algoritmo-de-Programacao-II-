numero = int(input("Digite um numero: "))

soma = 0
letra = str(numero)

for i in range(len(letra)):
    
    soma += int(letra[i])
print(soma)

