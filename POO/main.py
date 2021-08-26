from veiculo import Veiculo
from veiculo import Carro

moto = Veiculo("azul", 2, "bmw", 30)

print("Moto")

print("Cor:",moto.cor)
print("Tanque:",moto.tanque)


moto.Abastecer(45)

print("Tanque:",moto.tanque)


carro = Carro("Vermelho",4,"ford", 50,200)

print("")
print("Carro")


print("Cor:",carro.cor)
print("Tanque:",carro.tanque)
print("Velocidade:",carro.velocidade)
