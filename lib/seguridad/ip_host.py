import socket
from colorama import init, Fore

init()
r = Fore.RED
v = Fore.GREEN
p = Fore.LIGHTMAGENTA_EX
c = Fore.CYAN
reset = Fore.RESET

def obtenerIp(dominio):
    try:
        ipGet = socket.gethostbyname(dominio)
        print(f"{p}{dominio} {reset}==> {c}{ipGet}{reset}")
    except socket.gaierror:
        print(f"{r}[x] Website no found{reset}")

dominio = input(f"{r}[{v}+{r}] {v}INGRESE EL DOMINIO: ")
obtenerIp(dominio)