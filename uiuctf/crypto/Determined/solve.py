from Crypto.Util.number import *
from itertools import permutations
import numpy as np
import socket
import ssl
import socket
import ssl

hostname = 'determined.chal.uiuc.tf'
port = 1337
n = 158794636700752922781275926476194117856757725604680390949164778150869764326023702391967976086363365534718230514141547968577753309521188288428236024251993839560087229636799779157903650823700424848036276986652311165197569877428810358366358203174595667453056843209344115949077094799081260298678936223331932826351
e = 65535
c = 72186625991702159773441286864850566837138114624570350089877959520356759693054091827950124758916323653021925443200239303328819702117245200182521971965172749321771266746783797202515535351816124885833031875091162736190721470393029924557370228547165074694258453101355875242872797209141366404264775972151904835111

def sock_connect(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.create_default_context()
    conn = context.wrap_socket(sock, server_hostname=hostname)
    conn.connect((hostname, port))
    return conn


#The trick is to get the result (which is the determinant of the matrix) 
#that leads us to the primes so after some trial and error because am lazy i found 
#the input that gets me -r directly which is the following :
#get r:
conn = sock_connect(hostname, port)
print(f"Connected to {hostname}:{port}")
initial_output = conn.recv()
print("Initial output from server:")
print(initial_output.decode())

for i in range(9):
    print(i)
    if i in [0,3,4,6]:
        conn.sendall('0 \n'.encode())
        final_output = conn.recv()
    else:
        conn.sendall('1 \n'.encode())
        final_output = conn.recv()
    if i == 8:
        r = -int(final_output.decode()[16:])

print(r)
#then I found the input that gets me -r*p so i used it to find p
#get P:
conn = sock_connect(hostname, port)
print(f"Connected to {hostname}:{port}")
initial_output = conn.recv()
print("Initial output from server:")
print(initial_output.decode())

for i in range(9):
    print(i)
    if i in [0,1,3]:
        conn.sendall('0 \n'.encode())
        final_output = conn.recv()
    else:
        conn.sendall('1 \n'.encode())
        final_output = conn.recv()
    if i == 8:
        p = -int(final_output.decode()[16:])//r

print(p)
print(isPrime(p))
print(isPrime(n//p))
#returns True for both


#after finding the P and making sure it is a prime and  n div p is a prime also
#we had just to decrypt the cipher in the txt

phi = (p-1)*(n//p-1)
print(phi)
d = inverse(e,phi)
flag = long_to_bytes(pow(c,d,n))
print(flag)
#flag is uiuctf{h4rd_w0rk_&&_d3t3rm1n4t10n}

