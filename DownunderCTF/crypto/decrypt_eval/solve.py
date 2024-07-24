from Crypto.Cipher import AES
import os
from pwn import *
from Crypto.Util.number import *
from itertools import *
response=b""
s=b''
r=remote("2024.ductf.dev", 30020)
payload=0
i=1
result=b''
while payload <= 0xff:
	r.recvuntil(b"ct: ")
	print(s.decode()+long_to_bytes(payload).hex())
	r.sendline(s.decode()+long_to_bytes(payload).hex())
	response=r.recvline()
	print(response)
	if response == b'1'*i+b'\n':
		s+=long_to_bytes(payload).hex().encode()
		key=bytes_to_long(b'1')^payload
		print("GOT THE KEY",key)
		if i==1:
			b=bytes_to_long(b'F')^key
		if i==2:
			b=bytes_to_long(b'L')^key
		if i==3:
			b=bytes_to_long(b'A')^key
		if i==4:
			b=bytes_to_long(b'G')^key
		payload=-1
		i+=1
		result+=long_to_bytes(b).hex().encode()		
	if i==5:
		break
	payload+=1
r.sendline(result)
print(r.recvline())
#DUCTF{should_have_used_authenticated_encryption!}
		
	
	




