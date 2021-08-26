from random import randint
import time
import timeit
import os

inicio = timeit.default_timer()


cont = 0

while True:
    a = randint(0,10)
    b = randint(0,10)
    c = randint(0,10)
    d = randint(0,10)

    if(a == 10 and b == 10 and c == 10 and d == 10 ):
        print(a)
        print(b)
        print(c)
        print(d)
        
        
        break

    else:
        cont +=1
        print(cont)



fim = timeit.default_timer()
print(fim - inicio)
