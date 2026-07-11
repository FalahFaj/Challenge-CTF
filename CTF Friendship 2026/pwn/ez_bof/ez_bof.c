#include <stdio.h>
#include <string.h>

void print_flag() {
    char flag[64];
    FILE *f = fopen("flag.txt", "r");
    
    if (f == NULL) {
        printf("\nFile flag.txt gaada, Bikin dulu ya di folder yang sama.\n");
        return;
    }

    fgets(flag, sizeof(flag), f);
    printf("\nFlag: %s\n", flag);
    fclose(f);
}

int main() {
    int target = 0xdeadf00d;
    char buffer[32];

    printf("Nilai target saat ini: 0x%08x\n", target);
    printf("Coba ubah variabel target jadi deadbeef\n");
    printf("Masukkan inputmu: ");
    
    gets(buffer);

    if (target == 0xdeadbeef) {
        printf("\nGOKIL! Target berubah jadi: 0x%08x\n", target);
        print_flag();
    } else {
        printf("\nTarget masih: 0x%08x. Coba lagi bang!\n", target);
    }

    return 0;
}
