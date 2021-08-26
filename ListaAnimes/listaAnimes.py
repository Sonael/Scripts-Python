import os

def adicionarAnime():
    while(True):
        print("\nQual anime vôce desejaa adicionar/sair")
        adicionar  =  input(">")

        arq = open("bancoAnimes.txt",'r').read().splitlines()


        if(adicionar in arq):
            print("Anime já adicionado")

        elif(adicionar == "sair"):
            break;
        else:
            arq = open("bancoAnimes.txt",'a')
            arq.write(adicionar)
            arq.write("\n")
            arq.close()



def listarAnimes():
    animes = []
    size = os.path.getsize("bancoAnimes.txt")

    if(size == 0):
        print("\nAinda não foi adicionado nunhum anime\n")
    else:
        animes = arq = open('bancoAnimes.txt','r').read().splitlines()
        print("\nLista de animes adicionados")

        animes.sort()
        
        for i in animes:
            print(i)
        arq.close()


def removerAnime():

    size = os.path.getsize("bancoAnimes.txt")

    if(size == 0):
        print("\nAinda não foi adicionado nunhum anime\n")
    else:
        lista = []
        lista = arq = open('bancoAnimes.txt','r').read().splitlines()

        print("\nLista de Animes:")

        lista.sort()
        
        for i in lista:
            print(i)

        print("\n")

        print("Digite o nome do anime a ser deletado")
        animeDeletado = input(">")

        lista =  arq = open('bancoAnimes.txt','r').read().splitlines()

        


        try:
            lista.remove(animeDeletado)
                
            print("Anime removido\n")

            arq = open('bancoAnimes.txt','w')

            for i in lista:
                arq.write(i)
                arq.write("\n")
            arq.close()
        except:
            print("Digite um anime que está na lista")
            print("\n")
            

arq = open("bancoAnimes.txt",'a')



while(True):

    try:

        print("1-Adiconar animes\n2-Listar Animes\n3-Remover Animes")
        menu = int(input(">"))

        if(menu == 1):
            adicionarAnime()

        elif(menu == 2):
            listarAnimes()

        elif(menu == 3):
            removerAnime()
        else:
            print("\nDigite uma opção válida\n")
    except:
        print("\nDigite um valor válido\n")
        

