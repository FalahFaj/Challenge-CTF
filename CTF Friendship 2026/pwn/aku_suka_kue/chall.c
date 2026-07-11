#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>

void win() {
    char flag[64];
    int fd = open("flag.txt", O_RDONLY);
    if (fd != -1) {
        read(fd, flag, sizeof(flag));
        printf("\nPIE & Canary bypassed! JAGO BGT, Flag: %s\n", flag);
        close(fd);
    }
    exit(0);
}

void vuln() {
    char buffer[32];

    printf("Masukkan input untuk leak: ");
    read(0, buffer, 128);
    printf("Data kamu: %s\n", buffer);

    printf("Sekarang kasih payload terakhir: ");
    read(0, buffer, 128);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    vuln();
    return 0;
}
