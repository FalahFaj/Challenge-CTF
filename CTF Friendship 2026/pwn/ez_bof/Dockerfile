FROM kalilinux/kali-rolling

# Install dependencies
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y \
    socat \
    libc6:i386 \
    && rm -rf /var/lib/apt/lists/*

# Create challenge directory
WORKDIR /home/ctf

# Copy challenge files
COPY ez_bof .
COPY ez_bof.c .
COPY flag.txt .

# Set permissions
RUN chmod +x ez_bof && \
    chmod 444 flag.txt && \
    chmod 444 ez_bof.c

# Create non-root user for security
RUN useradd -m ctfuser && \
    chown -R root:root /home/ctf && \
    chmod 755 /home/ctf

USER ctfuser

# Expose port for remote connection
EXPOSE 2002

# Run the challenge with socat
CMD ["socat", "TCP-LISTEN:2002,reuseaddr,fork", "EXEC:/home/ctf/ez_bof"]
