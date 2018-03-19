def dec_bin(x,bini):
    while(True):
        bini = bini + str(x%2)
        x = x//2
        if x == 0:
            break
    bini = bini[::-1]
    b = int(bini)
    return b

bini = ""
x = -1
while x<0:
    x = int(input("Número:"))
    
print(dec_bin(x,bini))


#Rec

def dec_bin(x,bini):
    if x>0:
        bini = bini + str(x%2)
        x = x//2
        return dec_bin(x,bini)
    else:
        bini = bini[::-1]
        b = int(bini)
        return b

bini = ""
x = -1
while x<0:
    x = int(input("Número:"))  
print(dec_bin(x,bini))
