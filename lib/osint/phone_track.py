import requests
from time import sleep
import json
import colorama
from colorama import Fore,init

verde = Fore.GREEN
cyan = Fore.CYAN
rojo = Fore.RED
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
blanco = Fore.WHITE
reset = Fore.RESET
yellow = Fore.YELLOW
blue = Fore.BLUE

sleep(1)

banner="""
·▄▄▄▄        ▐▄• ▄  ▄▄▄· ▄ .▄       ▐ ▄ ▄▄▄ .
██▪ ██ ▪      █▌█▌▪▐█ ▄███▪▐█▪     •█▌▐█▀▄.▀·
▐█· ▐█▌ ▄█▀▄  ·██·  ██▀·██▀▐█ ▄█▀▄ ▐█▐▐▌▐▀▀▪▄
██. ██ ▐█▌.▐▌▪▐█·█▌▐█▪·•██▌▐▀▐█▌.▐▌██▐█▌▐█▄▄▌
▀▀▀▀▀•  ▀█▄▀▪•▀▀ ▀▀.▀   ▀▀▀ · ▀█▄▀▪▀▀ █▪ ▀▀▀ 
"""

print (verde+banner)

print (rojo+"INGRESE EL NÚMERO (EJ:+5491188888888):")

try:
       numero=int(input("---> "+reset))
except ValueError:
       print ("porfavor ingrese solamente numeros.")

print (magenta+"sacando información de el número...")

API_KEY='71c9a91b73291f84764eda1c5ccba175'

try:
       url = 'http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1' % (API_KEY, numero)
       session=requests.Session()
       headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 OPR/73.0.3856.284',
              'Accept':'text/html,application/xhtml+xml,application/xml;'
              'q=0.9,image/webp,*/*;q=0.8'}
       req = session.get(url, headers=headers)
       response=req.json()
       
       valid=response['valid']
       number=response['number']
       formato_local=response['local_format']
       formato_internacional=response['international_format']
       prefijo_origen=response['country_prefix']
       prefijo_codigo=response['country_code']
       nombre_origen=response['country_name']
       localizacion=response['location']
       empresa=response['carrier']
       tipo_linea=response['line_type']

       print (blue+"***************************************************************")
       print (cyan+f"valido: {valid}")
       print (cyan+f"numero: {number}")
       print (cyan+f"formato local: {formato_local}")
       print (cyan+f"formato internacional: {formato_internacional}")
       print (cyan+f"prefijo: {prefijo_origen}")
       print (cyan+f"codigo de origen: {prefijo_codigo}")
       print (cyan+f"nombre del pais: {nombre_origen}")
       print (cyan+f"nombre de la provincia: {localizacion}")
       print (cyan+f"empresa: {empresa}")
       print (cyan+f"tipo de linea: {tipo_linea}")
       print (blue+"***************************************************************")
except NameError:
       print ("el numero que ingreso es incorrecto, porfavor vuelva a intentarlo")
