FROM ubuntu:22.04

# Install runtime dependencies 32-bit
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y socat libc6:i386 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /home/ctf

# Ambil hasil binary yang udah jadi dari STAGE 1
COPY ret2win .
COPY ret2win.c .
COPY flag.txt .

# Set permissions
RUN chmod +x ret2win && \
    chmod 444 flag.txt && \
    chmod 444 ret2win.c

# Create non-root user
RUN useradd -m ctfuser && \
    chown -R root:root /home/ctf && \
    chmod 755 /home/ctf

USER ctfuser
EXPOSE 2001

CMD ["socat", "TCP-LISTEN:2001,reuseaddr,fork", "EXEC:/home/ctf/ret2win"]
