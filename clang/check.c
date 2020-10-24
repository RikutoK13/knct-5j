//
// Created by user on 2020/08/25.
//

#include <stdio.h>
#include <stdlib.h>

int main() {
    srand(1);
    printf("%d\n", (rand() % 6) + 1);
    srand(10);
    printf("%d\n", (rand() % 6) + 1);
    srand(15);
    printf("%d\n", (rand() % 6) + 1);
    srand(11);
    printf("%d\n", (rand() % 6) + 1);
    printf("%d\n", (rand() % 6) + 1);

}
