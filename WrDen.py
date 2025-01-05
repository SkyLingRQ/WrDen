import os
from colorama import Fore,init
import platform

v = Fore.GREEN
cyan = Fore.CYAN
r = Fore.RED
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

banner_help = """
   phone_dox     :   Datos de un número telefónico
      
   ip_hosts     :   Identificar la ip de un sitio web
   
   ip_track        :   Datos de una dirección ip pública
   
   scan_port     :   Escaneo total de puertos hacia una ip
   
   fake_name      :   Generar Identidad Falsa
      
   search_user    :   Realizar una busqueda de un username en distintas redes sociales
   
   hash_encrypted   :   Hashear textos en variedades de tipos de hash. Se incluye encriptación por bcrypt
   
   help   :  Mostrar menú de opciones 
   
   exit  : Salir del programa
   
   clear  :  Limpiar la pantalla
"""

banner = f"""

{r}                                                 W   R   D   E   N   T   O   O   L   K   I   T



                                                                      {blue}  Wrd
                                                            {cyan}           _    _
                                                                {cyan}      ((___))
                                                                {cyan}      [ x x ]
                            {blue}                                 Wrd {cyan}      \   /       {blue} Wrd
                                                                {cyan}       (' ')
                                                                {cyan}        (U)

{v}                                                 '..and none but the Bovine survived the onslaught'

{v}                                                       -Wrd-   CULT OF THE DEAD COW   -Wrd-
{v}                                                                   WrDen Toolkit
{v}                                                           -Wrd-   BASE SYSTEM   -Wrd-
{v}                                                            ---------------------------

{r}                                                                   HAVE A NICE DAY
                                    {v}----------------------- ------------ --------- -------- ------ ---- -- - - - -
                                    {r}#GITHUB: https://github.com/SkyLingRQ
                                    {r}#AUTHOR: SkyLing
                                    {v}- -   - - - - -  -- --- ------- -------- ------------ ------------------------

"""


try:
    print(banner)
    while True:
        op=input(f"{v}[{r}+{v}]{reset}~WrDen: ")
        if op =="help":
            print(banner_help)
        elif op=="ip_track":
            import lib.osint.ip_track
        elif op=="phone_dox":
            import lib.osint.phone_track
        elif op=="scan_port":
            import lib.seguridad.scan_ports
        elif op=="fake_name":
            import lib.Anonimato.fake_name
        elif op=="search_user":
            os.system("cd lib && cd osint && bash search_user.sh")
        elif op=="ip_hosts":
            import lib.seguridad.ip_host
        elif op=="hash_encrypted":
            import lib.seguridad.hash_encrypted
        elif op=="exit":
            exit()
        elif op=="clear":
            if plataforma == "Linux":
                    os.system("clear")
                    print(banner)
            elif plataforma == "Windows":
                os.system("cls")
                print(banner)
            else:
                print (f"[{r}x{reset}] Error: Plataforma Inrreconocible")
        else:
            print (f"{blue}[{r}!{blue}] {reset}Option Not Found")
            continue
except KeyboardInterrupt:
    print (yellow+"\nSaliendo Del Programa..")
