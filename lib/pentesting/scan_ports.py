import socket
import sys
import os
from time import sleep
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

banner = f"""
{blue}   _____                 _____           _       
{blue}  / ____|               |  __ \         | |      
{blue} | (___   ___ __ _ _ __ | |__) |__  _ __| |_ ___ 
{blue}  \___ \ / __/ _` | '_ \|  ___/ _ \| '__| __/ __| {verde}        WrDen
{blue}  ____) | (_| (_| | | | | |  | (_) | |  | |_\__ \  {rojo} ======================
{blue} |_____/ \___\__,_|_| |_|_|   \___/|_|   \__|___/   {cyan}   Scanner Of Ports
                                             
"""
print (banner)
ip_addr = input(verde+"IP Target: ")
portList = [0,21,22,23,25,53,67,68,69,80,88,161,162,500,514,101,110,123,137,138,139,143,179,194,443,445,587,591,853,990,993,995,1194,1701,1723,1812,1813,1813,2049,2082,2083,3074,3306,3389,4500,4662,4672,4899,5000,5400,5500,5600,5700,5800,5900,6881,6969,8080,51400,25565,51871,8443,111,49191,2525,4444,2095,2096,2077,2078,2082,2083,2087,2222,1111,8000,8999,9418,9100,5353.5351,5228,5297,5350,3031,3283,3284,3285,631,636,749]

for port in portList:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"{yellow}Puerto: {port} - {verde}OPEN")
        else:
            print(f"{yellow}Puerto: {port} - {rojo}CLOSED")
        sock.close()
    except socket.error as err:
        print(f"Error De Conexion: {err}")
        sys.exit()