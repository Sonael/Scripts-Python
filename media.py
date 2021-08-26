while True:

    a = float(input("Primeira  nota: "))
    b = float(input("Segunda  nota: "))
    c = float(input("Terceira  nota: "))
    d = float(input("Quarta  nota: "))

    x = (a+b+c+d)/4


    print('media: ',x)

    print('='*10)
    if x >= 6:
        print("aprovado")
    else:
        print("reprovado")
    print('='*10)
        

