import requests
import colorama
from colorama import Fore,init
import os

v = Fore.GREEN
cyan = Fore.CYAN
r = Fore.RED
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
blanco = Fore.WHITE
reset = Fore.RESET
yellow = Fore.YELLOW
blue = Fore.BLUE

os.system("cls")

user = input("usuario a buscar: ")

url = 'https://www.instagram.com/'+user
session=requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;'
'q=0.9,image/webp,*/*;q=0.8'}
req = session.get(url, headers=headers)
print (req)
if req==:
    print ("el usuario existe")
else:
    print ("el usuario no existe")