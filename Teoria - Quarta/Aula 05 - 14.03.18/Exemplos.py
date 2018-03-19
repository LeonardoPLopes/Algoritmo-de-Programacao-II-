lista = ['Macarrão','Morango','Laranja','Uva','Chocolate']

posição=len(lista)

print(lista)
print("")
print('Sua lista possui {} objetos!'.format(len(lista)))
print('O segundo objeto é: {}'.format(lista[1]))
print('O ultimo objeto é: {}'.format(lista[len(lista)-1]))
print("")

lista.insert(4, 'melão')#Inserir
print(lista)
print("")

del lista[0]#Deleta
print(lista)
print("")

lista.append('mel')#coloca por ultimo
print(lista)
