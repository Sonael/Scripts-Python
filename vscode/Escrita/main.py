import pywhatkit as kit
from translate import Translator

info = kit.info('brazil',lines=10,return_value=True)
#translator = Translator(from_lang="english",to_lang="portuguese")

#tranlation = translator.translate(info)
kit.text_to_handwriting(info,save_to="pywhatkit.png")


