import time

t = 0
h = 0
def aa():
    global t
    global h
    while True:
        x = input("você quer que o ano acabe?")
        if x == 'sim' or x == 's':
            t += 1
            return t
        elif x == 'não' or x == 'nao' or x == 'n':
            h += 1
            return h
        else:
            print('='*10)
            print('por favor responda com sim ou não')
            print('='*10)
            
while True:
    aa()
    print('='*10)
    print('sim: ',t)
    print('não: ',h)
    print('='*10)
