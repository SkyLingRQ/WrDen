import socket
import sys
import json
import requests
from time import sleep
import os
import colorama
from colorama import Fore,init
import platform

v = Fore.GREEN
cyan = Fore.CYAN
r = Fore.RED
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
blanco = Fore.WHITE
reset = Fore.RESET
yellow = Fore.YELLOW
blue = Fore.BLUE

plataforma = platform.system()

if plataforma == "Linux":
    os.system("clear")
elif plataforma == "Windows":
    os.system("cls")
else:
    print (f"[{r}x{reset}] Plataforma Inrreconocible")

def modulos():
    print (reset+"""
   phone_dox     :   Datos de un número telefónico. 
   
   system_ip    :   Identificar sistema operativo por la dirección ip.
   
   ip_hosts     :   Identificar la ip de un sitio web
   
   ip_track        :   Datos de una dirección ip pública.
   
   scan_port     :   Encontrar los puertos abiertos de un host
   
   fake_name      :   Generar Identidad Falsa
   
   ddos_attack    :   Realizar un ataque ddos a una web
   
   search_user    :   Realizar una busqueda de un nombre en distintas redes sociales
   
   sms_anom       :    Enviar SMS Anonimamente
   
   hash_encrypted   :   Encriptar textos en varios tipos de hash
   
   help   :  Mostrar menú de opciones. 
   
   exit  : salir del programa
   
   clear  :  Limpiar la pantalla
""")

#ip track
def ip_track():
    import lib.osint.ip_track
    opciones()

#phone track

def phone_track():
    import lib.osint.phone_track
    opciones()
    
#scan ports

def scan_ports():
    import lib.pentesting.scan_ports
    opciones()
            
#sistem_ip
def system_ip():
    direccion_ip = input("IP: ")
    os.system(f"cd lib && cd osint && python sistem_ip.py {direccion_ip}")
    opciones()
    
def fake_name():
    import lib.Anonimato.fake_name
    opciones()

def ddos_attack():
    import lib.pentesting.attack_ddos_dos
    opciones()

def sms_anom():
    os.system("cd lib && cd Anonimato && bash sms_anom.sh")
    opciones()

def search_user():
    os.system("cd lib && cd osint && bash search_user.sh")
    opciones()

def ip_hosts():
    import lib.pentesting.ip_host
    opciones()

def hash_encrypted():
    import lib.pentesting.hash_encrypted
    opciones()

banner = f"""

{r}                                                 W   R   D   E   N   T   O   O   L   H   K



                                                                    {blue}  Wrd
                                                            {cyan}       _   _
                                                            {cyan}      ((___))
                                                            {cyan}      [ x x ]
                        {blue}                                 Wrd {cyan}      \   /       {blue} Wrd
                                                            {cyan}       (' ')
                                                            {cyan}        (U)

{v}                                                     '..and none but the Bovine survived the onslaught'

{v}                                                         -Wrd-   CULT OF THE DEAD COW   -Wrd-
{v}                                                                     WrDen Toolkit
{v}                                                             -Wrd-   BASE SYSTEM   -Wrd-
{v}                                                             ---------------------------

{r}                                                                   HAVE A NICE DAY
                                    {v}----------------------- ------------ --------- -------- ------ ---- -- - - - -
                                    {r}#GITHUB: https://github.com/SkyLingRQ
                                    {r}#INSTAGRAM: https://www.instagram.com/skt.skyling014
                                    {r}#AUTHOR: SkyLing
                                    {v}- -   - - - - -  -- --- ------- -------- ------------ ------------------------

"""


print (banner)
sleep(1)

def opciones():
    try:
        op=input(f"{v}[{r}+{v}]{reset}~WrDen: ")
        if op =="help":
            modulos()
            opciones()
        elif op=="ip_track":
            ip_track()
        elif op=="phone_dox":
            phone_track()
        elif op=="scan_port":
            scan_ports()
        elif op=="system_ip":
            system_ip()
        elif op=="fake_name":
            fake_name()
            opciones()
        elif op=="ddos_attack":
            ddos_attack()
        elif op=="sms_anom":
            sms_anom()
        elif op=="search_user":
            search_user()
        elif op=="ip_hosts":
            ip_hosts()
        elif op=="hash_encrypted":
            hash_encrypted()
        elif op=="exit":
            print (yellow+"Adios :'("+reset)
            os.system("exit")
        elif op=="clear":
            if plataforma == "Linux":
                os.system("clear")
                opciones()
            elif plataforma == "Windows":
                os.system("cls")
                opciones()
            else:
                print (f"[{r}x{reset}] Error: Plataforma Inrreconocible")
                opciones()
        else:
            print (f"{blue}[{r}!{blue}] {reset}Option Not Found")
            opciones()
    except KeyboardInterrupt:
        print (yellow+"\nSaliendo Del Programa..")
        sleep(1.5)



opciones()