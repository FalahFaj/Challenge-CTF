#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>

void win() {
    char flag[64];
    printf("\nGG! Canary kebongkar\n");

    int fd = open("flag.txt", O_RDONLY);
    if (fd == -1) {
        printf("flag.txt nggak ketemu bang!\n");
        exit(1);
    }

    read(fd, flag, sizeof(flag));

    printf("Isi flagnya: ");
    write(1, flag, sizeof(flag));

    close(fd);

    exit(0);
    exit(0);
}

void vuln() {
    char buffer[32];

    printf("Siapa namamu bang? ");
    read(0, buffer, 128);
    printf("Halo: %s\n", buffer);

    printf("Ada pesan terakhir? ");
    read(0, buffer, 128);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    vuln();
    return 0;
}
