//
// Created by user on 2020/08/29.
//

#include <stdio.h>

#define N 1024

struct item {
    char id[8];
    int math;
    int eng;
};

int readfile(int n, struct item table[N]);
void make_ranking(int size, int rank[], struct item table[N]);

int main() {
    struct item table[N];
    int rank[N];
    // int size = readfile(N, table);
    int size = N;

}


void make_ranking(int size, int rank[], struct item table[N]) {

}
