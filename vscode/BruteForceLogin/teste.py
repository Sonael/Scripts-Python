arquivo  = open("senhas.txt")

linhas = arquivo.readlines()

for linha in linhas:
    if(linha.split("\n")[0] == "159951Pc"):
        print("tem igual")

