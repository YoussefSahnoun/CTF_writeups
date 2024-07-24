from Crypto.Util.number import *
import operator

with open("key.png","rb") as f:
	ct=f.read()
key="0x21a"
print(long_to_bytes(operator.xor(bytes_to_long(ct),int(key,16)))[:200])