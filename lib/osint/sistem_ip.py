#!/usr/bin/python3

import subprocess,re,sys
from colorama import *

r = Fore.RED
res = Fore.RESET

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    DARKCYAN = '\033[36m'
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


def arguments():
    print (f"[{r}x{res}] Ocurrió Un Error")
    sys.exit(1)


def get_value_ttl(ip_address):
    proc = subprocess.Popen(["ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    out = out.split()
    out = out[12].decode('utf-8')

    ttl = re.findall(r"\d{1,3}", out)[0]

    return ttl


if __name__ == '__main__':
    try:
        ip_address = sys.argv[1]

        ttl_value = get_value_ttl(ip_address)
        ttl_value = int(ttl_value)

        if ttl_value >= 0 and ttl_value <= 64:
            print(bcolors.BOLD + "\n%s -> " % ip_address + bcolors.GREEN + "Linux \n" + bcolors.ENDC)
        elif ttl_value >= 65 and ttl_value <= 128:
            print(bcolors.BOLD + "\n%s -> " % ip_address + bcolors.GREEN + "Windows \n" + bcolors.ENDC)
        else:
            print(bcolors.BOLD + "\n%s -> " % ip_address + bcolors.GREEN + "Solaris/AIX\n" + bcolors.ENDC)
    except:
        arguments()