def MDC():
    primeiro = int(input("Digite um numero inteiro: "))
    segundo = int(input("Digite outro numero inteiro: "))

    mdc = primeiro
    while primeiro % mdc != 0 or segundo % mdc != 0: 
        mdc = mdc - 1

    print("MDC(%d,%d)=%d" %(primeiro,segundo,mdc))
MDC()        
