# -*- coding: utf-8 -*-
from flask import Flask
import paramiko

app = Flask(__name__)

host = input("Host= ")
user = input('User= ')
port = input('Port= ')
passwd = input('Password= ')
print("################")
comando = input('Comando= ')

@app.route("/resposta.py")

def get_x():

    global host
    global user
    global passwd
    global comando
    global port

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(host, username=user, password=passwd, port=port)  # quando entra vai esta na pasta padrão
        client.exec_command(comando)
        return 'comando enviado'
    except Exception as erro:
        return erro



if __name__ == "__main__":
    app.run()
