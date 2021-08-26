from random import choice

arq = open('arquivo.txt', 'w')

perg = input('Pegunta de sim ou não: ')

lista = ['sim\n','não\n']

a = 0

while a<100000:
    x = choice(lista)
    arq.write(x)
    a+=1

arq.close()


arq = open('arquivo.txt', 'r')

texto = arq.readlines()

sim = 0
nao = 0

for linha in texto:
    if linha == 'sim\n':
        sim +=1
    elif linha == 'não\n':
        nao +=1
arq.close()

print('Sim: ', sim)
print('Não: ', nao)

if sim > nao:
    print('\nSim')
else:
    print('\nNão')
    
