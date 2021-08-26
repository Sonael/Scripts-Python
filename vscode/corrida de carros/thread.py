from threading import Thread
from time import sleep

class carro:
    def __init__(self,nome, velocidade):
        super().__init__()
        self.nome = nome
        self.velocidade = velocidade
        self.distancia = 0

    def getVelociade(self):
        return self.velocidade

    def getNome(self):
        return self.nome


    def corrida(self,pista):
        while(self.distancia <= pista.getTamanho()):
            self.distancia += self.velocidade
            # print("o "+carro.getNome()+" esta em "+str(self.distancia))
            sleep(1)

        print("o "+ self.nome +" utrapassou a linha de chegada")


class pista:
    def __init__(self,tamanho):
        super().__init__()
        self.tamanho = tamanho

        

    def getTamanho(self):
        return self.tamanho


carro1 = carro("carro1", 80)
carro2 = carro("carro2",100)

pista = pista(1000)

# carro1_corrida = Thread(target=carro1.corrida,args=[pista])

# carro2_corrida = Thread(target=carro2.corrida,args=[pista])


# carro1_corrida.start()
# carro2_corrida.start()

string = "olá mundo"








