#############################
# OBS the encryption is     #
# random and will be gone   #
# when the program restarts.#
# Don't use this for real   #
#############################

import random

encrypt = {}
decrypt = {}
chars = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']

securitylevel = 32

def derflas_encryption(x):
    if x in encrypt:
        return encrypt[x]
    else:
        str = ''
        for a in range(securitylevel):
            str += random.choice(chars)
        encrypt[x]=str
        decrypt[str] = x
        return str

def derflas_decrypt(str):
    if str in decrypt:
        return decrypt[str]
    else:
        return None

crypting = True

while crypting:
    sort = input("encrypt or decrypt?? (e/d)")
    if sort == 'd' or sort == 'D':
        print(derflas_decrypt(input("text to decrypt")))
    if sort == 'e' or sort == 'E':
        print(derflas_encryption(input("text to encrypt"))) 
