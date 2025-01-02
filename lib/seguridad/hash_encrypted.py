#encriptacion con hashlib
#AUTHOR: SKYLING
import bcrypt
import sys
import colorama
from colorama import Fore,init
import time

v = Fore.GREEN
cyan = Fore.CYAN
r = Fore.RED
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
blanco = Fore.WHITE
reset = Fore.RESET
a = Fore.YELLOW
b = Fore.BLUE

banner = f"""

             {r}   HashEncrypted
        {v} [+] {b}-------------------- {v}[+]
             {r}   By SkyLingRQ


   {a} [1] cifrado blake2b
    {a}[2] cifrado blake2s
    {a}[3] cifrado md5
    {a}[4] cifrado sha1
    {a}[5] cifrado sha224
    {a}[6] cifrado sha256
    {a}[7] cifrado sha3_224
    {a}[8] cifrado sha3_256
    {a}[9] cifrado sha3_384
    {a}[10] cifrado sha3_512
    {a}[11] cifrado sha512
    {a}[12] cifrado bcrypt
    

"""

for i in banner:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.02)

try:
    text = int(input(f"{b}[{r}${b}] {v}HASH --> "))
except ValueError:
    print ("Opcion Incorrecta")
if text==1:
    import hashlib
    from hashlib import blake2b
    a = input(f"{b}[{r}#{b}] {v}TEXT TO HASH --> ")
    print (cyan+"[#] HASH GENERATED: "+v)
    print(blake2b(a.encode("utf-8")).hexdigest())
elif text==2:
    import hashlib
    from hashlib import blake2s
    a = input(f"{b}[{r}#{b}] {v}TEXT TO HASH --> ")
    print (cyan+"[#] HASH GENERATED: "+v)
    print (blake2s(a.encode("utf-8")).hexdigest())
elif text==3:
    import hashlib
    from hashlib import md5
    a = input(f"{b}[{r}#{b}] {v}TEXT TO HASH --> ")
    print (cyan+"[#] HASH GENERATED: "+v)
    print (md5(a.encode("utf-8")).hexdigest())
elif text==4:
    import hashlib
    from hashlib import sha1
    a = input(f"{b}[{r}#{b}] {v}TEXT TO HASH --> ")
    print (cyan+"[#] HASH GENERATED: "+v)
    print (sha1(a.encode("utf-8")).hexdigest())
elif text==5:
    import hashlib
    from hashlib import sha224
    a = input(f"{b}[{r}#{b}] {v}TEXT TO HASH --> ")
    print (cyan+"[#] HASH GENERATED: "+v)
    print (sha224(a.encode("utf-8")).hexdigest())
elif text==6:
    import hashlib
    from hashlib import sha256
    a = input(f"{b}[{r}#{b}] {v}TEXT TO HASH --> ")
    print (cyan+"[#] HASH GENERATED: "+v)
    print (sha256(a.encode("utf-8")).hexdigest())
elif text==7:
    import hashlib
    from hashlib import sha3_224
    a = input(f"{b}[{r}#{b}] {v}TEXT TO HASH --> ")
    print (cyan+"[#] HASH GENERATED: "+v)
    print (sha3_224(a.encode("utf-8")).hexdigest())
elif text==8:
    import hashlib
    from hashlib import sha3_256
    a = input(f"{b}[{r}#{b}] {v}TEXT TO HASH --> ")
    print (cyan+"[#] HASH GENERATED: "+v)
    print (sha3_256(a.encode("utf-8")).hexdigest())
elif text==9:
    import hashlib
    from hashlib import sha3_384
    a = input(f"{b}[{r}#{b}] {v}TEXT TO HASH --> ")
    print (cyan+"[#] HASH GENERATED: "+v)
    print (sha3_384(a.encode("utf-8")).hexdigest())
elif text==10:
    import hashlib
    from hashlib import sha3_512
    a = input(f"{b}[{r}#{b}] {v}TEXT TO HASH --> ")
    print (cyan+"[#] HASH GENERATED: "+v)
    print (sha3_512(a.encode("utf-8")).hexdigest())
elif text==11:
    import hashlib
    from hashlib import sha512
    a = input(f"{b}[{r}#{b}] {v}TEXT TO HASH --> ")
    print (cyan+"[#] HASH GENERATED: "+v)
    print (sha512(a.encode("utf-8")).hexdigest())
elif text==12:
    a = input(f"{b}[{r}#{b}] {v}TEXT TO HASH --> ")
    bc = bcrypt.hashpw(a.encode('utf-8'), bcrypt.gensalt())
    print (cyan+"[#] HASH GENERATED: "+v)
    print(bc)
else:
    print (reset+"Opcion No Encontrada")