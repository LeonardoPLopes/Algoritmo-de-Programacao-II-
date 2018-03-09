num=int(input("Digite uma sequência de números inteiros: "))
maior=num
menor=num

while num >= 0:
    if maior < num:
        maior=num
        print("Seu maior numero é: ",maior)
        print("Seu menor numero é: ",menor)
        num=int(input("Digite uma sequência de números inteiros: "))
    elif menor > num:
        menor=num
        print("Seu maior numero é: ",maior)
        print("Seu menor numero é: ",menor)
        num=int(input("Digite uma sequência de números inteiros: "))
    else:
        print("Seu maior numero é: ",maior)
        print("Seu menor numero é: ",menor)
        num=int(input("Digite uma sequência de números inteiros: "))

    

