from  pwn import *
import time
from Crypto.Util.number import *
from sympy.ntheory import discrete_log
while True:
    r = remote("ctf.mf.grsu.by", 9030)
    print(r.recvuntil(b"choice:"))
    r.sendline(b"1")
    print(r.recvuntil(b"p = "))
    p=int(r.recvline().strip())
    r.recvuntil(b"h = ")
    h=int(r.recvline().strip())
    print(p)
    print(h)
    x=discrete_log(p,h,2)
    print(x)
    flag=f"grodno{long_to_bytes(x)}"
    print(flag)
    '''r.sendline(b"2")
    r.sendline(flag)
    print(r.recvline())'''