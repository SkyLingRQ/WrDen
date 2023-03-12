import requests
from time import sleep
import json
import colorama
from colorama import Fore,init
import os

v = Fore.GREEN
c = Fore.CYAN
r = Fore.RED
lr = Fore.LIGHTRED_EX
m = Fore.MAGENTA
lm = Fore.LIGHTMAGENTA_EX
b = Fore.WHITE
reset = Fore.RESET
a = Fore.YELLOW
az = Fore.BLUE

sleep(1)

banner = f""" o            o
{a}  \          /
{a}   \        /
{a}    :-'""'-:
{a} .-'  ____  `-.   {v}          WrDen
{a}( (  (_()_)  ) )  {r}   ======================
{a} `-.   ^^   .-'   {az}     Ip Tracker Tool
{a}    `._==_.'
{r}WrD {a} __)(___

"""



print (a+banner)
sleep(1.5)

ip = input(c+"IP Target : ")
print (f"la ip a trackear es: {ip}")
print ("Aguarde Un Momento...")
sleep(1)
url = 'http://ip-api.com/json/'+str(ip)
session=requests.Session()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 OPR/73.0.3856.284',
   'Accept':'text/html,application/xhtml+xml,application/xml;'
   'q=0.9,image/webp,*/*;q=0.8'}

req = session.get(url, headers=headers)
response=req.json()
print (a+"")
try:
       status=response['status']
       country=response['country']
       countryCode=response['countryCode']
       region=response['region']
       region_name=response['regionName']
       city=response['city']
       zip=response['zip']
       lat=response['lat']
       lon=response['lon']
       timezone=response['timezone']
       isp=response['isp']
       org=response['org']
       ass=response['as']


       print (f"estado: {status}")
       print (f"pais: {country}")
       print (f"codigo del pais: {countryCode}")
       print (f"region: {region}")
       print (f"nombre de la region: {region_name}")
       print (f"ciudad: {city}")
       print (f"zip: {zip}")
       print (f"latitud: {lat}")
       print (f"longitud: {lon}")
       print (f"tiempo de zona: {timezone}")
       print (f"isp: {isp}")
       print (f"org: {org}")
       print (f"as: {ass}")
except KeyError:
       print (m+"ingrese caracteres validos.")
       print ("ejemplo: 142.251.133.206")
       print (reset)