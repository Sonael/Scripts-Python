#class Veiculo
class Veiculo:

    def __init__(self,cor,rodas,marca,tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def Abastecer(self,litros):

        qnt = self.tanque + litros
        if(qnt < 100):
            self.tanque += litros
            print(f"Tanque Abastecido em {litros} litros")
        else:
            print("Não pode abastecer mais do que o limite")

#class carro
class Carro(Veiculo):

     def __init__(self, cor,rodas,marca,tanque,velocidade):
         self.velocidade = velocidade
         Veiculo.__init__(self,cor,rodas,marca,tanque)
