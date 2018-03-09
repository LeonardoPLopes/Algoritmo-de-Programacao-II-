#Leonardo Pedro Lopes 31720528
#Descubrir o MMC

primeiro = int(input("Digite um número inteiro: "))
segundo = int(input("Digite outro número inteiro: "))

if primeiro > segundo:
    maior = primeiro
else:
    maior = segundo
while True:
    if maior % primeiro == 0 and maior % segundo == 0:
        print("O MMC é: ",maior)
        break
    else:
        maior += 1
        
