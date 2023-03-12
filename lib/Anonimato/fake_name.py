import requests
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
z = Fore.LIGHTBLACK_EX

banner = f"""     
{z}  ___/   \___
{z} /   '---'   \
{z} '--_______--'   {v}  WrDen
{v}       / \         {r}    ======================
{v}      /   \        {az}    Fake Identy Generator
{v}      /\O/\
{v}      / | \
{v}      // \\"""

print (banner)


url = 'https://api.namefake.com/'
session=requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 OPR/73.0.3856.284',
   'Accept':'text/html,application/xhtml+xml,application/xml;'
   'q=0.9,image/webp,*/*;q=0.8'}
req = session.get(url, headers=headers)
response=req.json()

name=response['name']
address=response['address']
latitude=response['latitude']
longitude=response['longitude']
maiden_name=response['maiden_name']
birth_data=response['birth_data']
phone_h=response['phone_h']
phone_w=response['phone_w']
email_u=response['email_u']
email_d=response['email_d']
username=response['username']
password=response['password']
domain=response['domain']
useragent=response['useragent']
ipv4=response['ipv4']
macaddress=response['macaddress']
plasticcard=response['plasticcard']
cardexpir=response['cardexpir']
bonus=response['bonus']
company=response['company']
color=response['color']
uuid=response['uuid']
height=response['height']
weight=response['weight']
blood=response['blood']
eye=response['eye']
hair=response['hair']
pict=response['pict']

print (c+"")
print (f"NAME: {name}")
print (f"ADDRESS: {address}")
print (f"LATITUDE: {latitude}")
print (f"LONGITUDE: {longitude}")
print (f"MAIDEN NAME: {maiden_name}")
print (f"PICT: {pict}")
print (f"EYE: {eye}")
print (f"HAIR: {hair}")
print (f"UUID: {uuid}")
print (f"MACADDRESS: {macaddress}")
print (f"IPV4: {ipv4}")
print (f"DOMAIN: {domain}")
print (f"BONUS: {bonus}")
print (f"CARDEXPIR: {cardexpir}")
print (f"BLOOD: {blood}")
print (f"HEIGHT: {height}")
print (f"WEIGHT: {weight}")
print (f"COLOR: {color}")
print (f"COMPANY: {company}")
print (f"PLASTICCARD: {plasticcard}")
print (f"USERAGENT: {useragent}")
print (f"USERNAME: {username}")
print (f"PASSWORD: {password}")
print (f"EMAIL D: {email_d}")
print (f"EMAIL U: {email_u}")
print (f"PHONE H: {phone_h}")
print (f"PHONE W: {phone_w}")
print (f"BIRTH DATA: {birth_data}")