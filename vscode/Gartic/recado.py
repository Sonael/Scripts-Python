
import  cloudscraper

url = 'https://gartic.com.br/perfil_recado.php'



cookies = {
	"__cfduid": "db804648247ad873966deef4ad79a0df71611319502",
	"__utma": "212885122.1023224719.1611319503.1613467116.1613716900.13",
	"__utmb": "212885122.32.10.1613716900",
	"__utmc": "212885122",
	"__utmt": "1",
	"__utmz": "212885122.1611319503.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
	"_fbp": "fb.2.1611319503727.1949961508",
	"aceita": "600ac8ce2640f",
	"aviso_regras": "ok",
	"desenho": "csse2plea9kp54pu7s1rf2qsj7",
	"FCCDCF": "[[\"AKsRol_hTmvPkI5-pk6yfAm07k-g6Iu0lijMPTAlgkOJSLUyLdV93deqdX4myfv2IC5q1382BmcL0DYFqbdgN6SVaN7DTqQ3M31NLJiMsD10QXlSOOGT0FHZwEL-SPcHDVxtjl2ktXnEfiC8KMSe9jIzHcZWwcFgpQ==\"],null,[\"[[],[],[],[],null,null,true]\",1613720931281],null]"
}

scraper = cloudscraper.create_scraper(  browser={
        'browser': 'firefox',
        'platform': 'windows',
		'mobile': False
    })


for i in range(0, 6):
    recado = "teste"+ str(i)
    dados = {'recado':recado,'loginDestino':'__paradox'}
    r = scraper.post(url, data=dados, cookies=cookies)

