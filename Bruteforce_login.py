import requests


url = "https://gartic.com.br/log_ajax.php?rand=1575079977954"

resposta = requests.post(url)

print(resposta.text)
