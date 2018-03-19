def bin_dec(x, deci):
    for c in range(tam):
        if x[c] == "1":
            deci = deci + 2**int(c)
    return deci

x = int(input("Número:"))
deci = 0
x = str(x)
x = x[::-1]
tam = len(x)
print(bin_dec(x, deci))

#Rec
def bin_dec(x, deci, c):
    if c < tam:
        if x[c] == "1":
            deci = deci + 2**int(c)
        return bin_dec(x, deci, c+1)
    else:
        return deci

c = 0
x = int(input("Número:"))
deci = 0
x = str(x)
x = x[::-1]
tam = len(x)
print(bin_dec(x, deci, c))
