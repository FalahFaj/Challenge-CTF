FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    socat \
    && rm -rf /var/lib/apt/lists/*

# Create challenge directory
WORKDIR /home/ctf

# Copy challenge files
COPY chall .
COPY chall.c .
COPY flag.txt .

# Set permissions
RUN chmod +x chall && \
    chmod 444 flag.txt && \
    chmod 444 chall.c

# Create non-root user for security
RUN useradd -m ctfuser && \
    chown -R root:root /home/ctf && \
    chmod 755 /home/ctf

USER ctfuser

# Expose port for remote connection
EXPOSE 2004

# Run the challenge with socat
CMD ["socat", "TCP-LISTEN:2004,reuseaddr,fork", "EXEC:/home/ctf/chall"]
