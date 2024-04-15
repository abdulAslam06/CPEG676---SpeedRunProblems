# coding: utf-8
from pwn import *
pr = process("./chall_09")
elf = ELF("./chall_09")
payload = ((xor(elf.string(elf.sym.key), b"\x69")) + b"\x00\n")
pr.send(payload)
pr.interactive()
pr.close()
