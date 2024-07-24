from pwn import *
import base64
from Crypto.Cipher import AES
dummy_flag=b"grodno{"+b"a"*40+b"}"
r = remote("ctf.mf.grsu.by",9016)

def get_padding_byte(r):
    for padding_byte in range():
        print (chr(padding_byte))
        payload=("}" + chr(padding_byte) * 15).encode()
        print(payload)
        r.sendline(base64.b64encode(payload))
        r.recvuntil(b'): ')
        enc_pad = base64.b64decode(r.recvline().strip())[:16]
        print("this is how it is encrypted:",enc_pad)
        print(len(enc_pad))
        r.sendline(base64.b64encode(b'a'))
        r.recvuntil(b'): ')
        enc=base64.b64decode(r.recvline().strip())
        print("this is the last 16 bytes of c: ",enc[48:64])
        print(len(enc[48:64]))
        if(enc_pad[:14] in enc[48:64]):
            print ("FOUND PADDING BYTE " , chr(padding_byte))
            return (chr(padding_byte))
flag=""
for i in range(30,130):
	print(chr(i))
	payload=(("d"+chr(i)*16).encode())
	r.sendline(base64.b64encode(payload))
	r.recvuntil(b'): ')
	enc = base64.b64decode(r.recvline().strip())
	print(enc[:16])
	print(enc[64:80])
	if enc[:16]==enc[64:80]:
		print("padding char is :", chr(i))
		break

'''for j in range(16):
	for i in range(0x20,0x7e):
		print(chr(i))
		payload=(b"a"*(16-j-1))
		r.sendline(base64.b64encode(payload))
		r.recvuntil(b'): ')
		enc_i = base64.b64decode(r.recvline().strip())[:16]
		print(enc_i)
		r.sendline(base64.b64encode(('a'*(16-j-1)+flag+chr(i)).encode()))
		r.recvuntil(b'): ')
		enc =base64.b64decode(r.recvline().strip())[:16]
		print(enc)
		if(enc_i == enc):
			print ("FOUND the right byte -----------------------" , chr(i))
			flag+=chr(i)   
			break 
	print("-------------flag---------------:",flag)'''

        
          
'''
cipher = AES.new(key, AES.MODE_ECB)
cip=cipher.encrypt(dummy_flag)
print("cip: ",cip)
msg=cipher.decrypt(cip)
print("msg: ",msg)
print("flag: ",cipher.decrypt(c))'''