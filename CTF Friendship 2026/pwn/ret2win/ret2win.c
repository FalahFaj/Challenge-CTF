#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void win() {
    char flag[100];
    FILE *f = fopen("flag.txt", "r");
    
    if (f == NULL) {
        printf("\nflag.txt nggak ada! Bikin dulu bang.\n");
        exit(0);
    }

    fgets(flag, sizeof(flag), f);
    printf("\nJago banget kamu bang %s\n", flag);
    fclose(f);
    exit(0);
}

void vuln() {
    char buffer[16]; 
    printf("coba browsing bang, ret2win itu apa\n");
    printf("Masukkan input: ");
    read(0, buffer, 100);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    vuln();
    return 0;
}
