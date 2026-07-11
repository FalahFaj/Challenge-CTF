#include <stdio.h>
#include <string.h>
#include <unistd.h>

void vuln() {
    char buffer[64];
    printf("Stack kamu ada di sekitar: %p\n", buffer);
    printf("Masukkan shellcode kamu: ");
    
    int n = read(0, buffer, 256);

    for (int i = 0; i < n - 1; i++) {
        if (buffer[i] == '\x0f' && buffer[i+1] == '\x05') {
            printf("DETEKSI VIRUS! Shellcode diblokir.\n");
            _exit(1);
        }
    }
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    vuln();
    return 0;
}
