import random
from time import sleep
import os
import sys

class Inimigo:
    def __init__(self,nome,vida,defesa):
        super().__init__()
        self.nome = nome
        self.vida = vida
        self.conjAtaques = ["ataque letal","ataque medio", "ataque fraco"]
        self.defesa = defesa
        self.vivo = True
        self.hp = vida



    def getNome(self):
        return self.nome

    def getVida(self):
        return self.vida


    def getDefesa(self):
        return self.defesa

    def getVivo(self):
        return self.vivo

    def setVivo(self,vivo):
        self.vivo = vivo


    def setVida(self, vida):
        self.vida += vida
        self.hp = self.vida

    def getHp(self):
        return self.hp

    def setHp(self,hp):
        self.hp = hp


    def ataca(self, Heroi):
        ataque =  random.choice(self.conjAtaques)

        if ataque == "ataque letal":
            print(self.nome+" deu um ataque letal em "+ Heroi.getNome()+" causando "+str(int(self.vida*50/100))+" de dano")
            if Heroi.getDefesa() >= int(self.vida*50/100):
                print("bloqueado")
            else:
                Heroi.vida -= int(self.vida*50/100)
            
        
        elif ataque == "ataque medio":
            print(self.nome+" deu um ataque medio em "+ Heroi.getNome()+" causando "+str(int(self.vida*30/100))+" de dano")
            if Heroi.getDefesa() >= int(self.vida*30/100):
                print("bloqueado")
            else:
                Heroi.vida -= int(self.vida*30/100)

        elif ataque == "ataque fraco":
            print(self.nome+" deu um ataque fraco em "+ Heroi.getNome()+" causando "+str(int(self.vida*10/100))+" de dano")
            if Heroi.getDefesa() >= int(self.vida*10/100):
                print("bloqueado")
            else:
                Heroi.vida -= int(self.vida*10/100)


        
                


class Heroi:

    def __init__(self,nome = "Anonimo",vida = 100,ataque =1,defesa= 1,stamina= 10):
        super().__init__()
        self.vida = vida
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.stamina = stamina
        self.vivo = True
        self.fugir = False

    def getNome(self):
        return self.nome

    def getVida(self):
        return self.vida

    def getDefesa(self):
        return self.defesa

    def getAtaque(self):
        return self.ataque

    def getVivo(self):
        return self.vivo

    def getStamina(self):
        return self.stamina

    def getFugir(self):
        return self.fugir

    def setFugir(self,fugir):
        self.fugir = fugir


    def setVida(self,vida):
        self.vida += vida 

    def setVivo(self, vivo):
        self.vivo = vivo

    def setAtaque(self,ataque):
        self.ataque += ataque

    def setDefesa(self,defesa):
        self.defesa += defesa

    def setStamina(self,stamina):
        self.stamina += stamina

    def atacar(self, Inimigo):
        print("1-Ataque Rapido\n2-Ataque Forte\n3-Fugir")
        resp = int(input())
        if(resp == 1):
            print("\n"+self.nome+" deu um ataque rapido em "+ Inimigo.getNome()+" causando "+ str(self.ataque)+" de dano\n")
            Inimigo.hp -= self.ataque
        elif(resp == 2):

            if(self.ataque == 1):
                print("\n"+self.nome+" deu um ataque forte em "+ Inimigo.getNome()+" causando "+ str(self.ataque+2)+" de dano"+"\n")
                Inimigo.hp -= self.ataque+2
                self.stamina -= 1
            else:
                print("\n"+self.nome+" deu um ataque forte em "+ Inimigo.getNome()+" causando "+ str(self.ataque*2)+" de dano\n")
                Inimigo.hp -= self.ataque*2
                self.stamina -= 1
        elif(resp == 3):

            print(self.nome+" fugiu de um "+Inimigo.getNome())
            print(self.nome+ " perdeu "+str(int(self.vida*10/100))+" de vida por ter fugido")
            self.vida -= int(self.vida*5/100)
            self.fugir = True


    def morrer(self,Inimigo):
        print("\n"+self.nome+" morreu pra um "+ Inimigo.getNome()+"\n")






    


def main(Heroi):
    Slime = Inimigo("Slime",10,1)
    Goblin = Inimigo("Goblin",15,1)
    while((Heroi.getVivo() == True) and (Heroi.getStamina() >0)):
        sleep(2)


        Mobs = [Slime, Goblin,"espada","escudo","pocao"]


        opcao = random.choice(Mobs)

        if(opcao == Slime):
            Slime.setVivo(True)
            print("Um Slime Apareceu")
            Heroi.setFugir(False)
            while((Slime.getVivo() == True) and (Heroi.getVivo() == True) and (Heroi.getFugir()== False)):


                print("\n")
                print("Status: "+Heroi.getNome())
                print("Vida "+str(Heroi.getVida()))
                print("Ataque "+str(Heroi.getAtaque()))
                print("Defesa "+ str(Heroi.getDefesa()))
                print("Stamina "+ str(Heroi.getStamina()))
                print("\n")

                print("\n")
                print("Status: "+Slime.getNome())
                print("Vida "+str(Slime.getHp()))
                print("\n")


                if(Slime.getHp() >0 and Heroi.getVida() > 0):
                    Heroi.atacar(Slime)
                    Slime.ataca(Heroi)

                elif(Heroi.getVida() <= 0):
                    Heroi.setVivo(False)
                    Heroi.morrer(Slime)


                elif(Slime.getHp()<=0):
                    Slime.setVivo(False)
                    print(Heroi.getNome()+" Derrotou "+Slime.getNome())
                    Heroi.setAtaque(1)
                    Heroi.setStamina(2)
                    Heroi.setDefesa(1)
                    Heroi.setVida(3)


                    Slime.setVida(5)

                    

        elif(opcao == Goblin):
            Goblin.setVivo(True)
            print("Um Globlin Apareceu")
            Heroi.setFugir(False)
            while((Goblin.getVivo() == True) and (Heroi.getVivo() == True) and (Heroi.getFugir()== False)):


                print("\n")
                print("Status: "+Heroi.getNome())
                print("Vida "+str(Heroi.getVida()))
                print("Ataque "+str(Heroi.getAtaque()))
                print("Defesa "+ str(Heroi.getDefesa()))
                print("Stamina "+ str(Heroi.getStamina()))
                print("\n")

                print("\n")
                print("Status: "+Goblin.getNome())
                print("Vida "+str(Goblin.getHp()))
                print("\n")

                if(Goblin.getHp() > 0 and Heroi.getVida() > 0):
                    Heroi.atacar(Goblin)
                    Goblin.ataca(Heroi)

                elif(Heroi.getVida() <= 0):
                    Heroi.setVivo(False)
                    Heroi.morrer(Goblin)

                elif(Goblin.getHp()<=0):
                    Goblin.setVivo(False)
                    print(Heroi.getNome()+" Derrotou "+Goblin.getNome())
                    Heroi.setAtaque(3)
                    Heroi.setStamina(2)
                    Heroi.setDefesa(1)
                    Heroi.setVida(5)

                    Goblin.setVida(5)

                    


        elif(opcao == "espada"):
                Heroi.setAtaque(1)
                print("Voce aprimou seu Ataque")
                print("\n\n")
                print("Status: "+Heroi.getNome())
                print("Vida "+str(Heroi.getVida()))
                print("Ataque "+str(Heroi.getAtaque()))
                print("Defesa "+ str(Heroi.getDefesa()))
                print("Stamina "+ str(Heroi.getStamina()))
                print("\n\n")
                
        elif(opcao == "escudo"):
                Heroi.setDefesa(1)
                print("Voce aprimou sua Defesa")
                print("\n\n")
                print("Status: "+Heroi.getNome())
                print("Vida "+str(Heroi.getVida()))
                print("Ataque "+str(Heroi.getAtaque()))
                print("Defesa "+ str(Heroi.getDefesa()))
                print("Stamina "+ str(Heroi.getStamina()))
                print("\n\n")
                
        elif(opcao == "pocao"):
                Heroi.setStamina(1)
                print("Voce aprimou sua Stamina")
                print("\n\n")
                print("Status: "+Heroi.getNome())
                print("Vida "+str(Heroi.getVida()))
                print("Ataque "+str(Heroi.getAtaque()))
                print("Defesa "+ str(Heroi.getDefesa()))
                print("Stamina "+ str(Heroi.getStamina()))
                print("\n\n")
                



            



param = sys.argv

if(len(param[1:]) == 0):
    heroi = Heroi()
else:
    heroi  = Heroi(param[1],int(param[2]),int(param[3]),int(param[4]),int(param[5]))


main(heroi)
