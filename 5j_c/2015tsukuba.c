//
// Created by user on 2020/08/22.
//

#include <stdio.h>
#include <stdlib.h>

int count;

void swap(int i, int j, int array[]);  // 簡単なのでとばす
int max_position(int n, int array[]);

int main() {
    count = 0;
    int a3[3] = {8, 10, 9};  // ここを自由に変えてcountの値を探る( (3-1) )
    int ans = max_position(3, a3);
    printf("%d\n", count);
    printf("answer:%d\n", ans);
}

int max_position(int n, int array[]) {
    count++;
    if (n > 1) {
        int p = max_position(n-1, array);
        printf("n:%d, p:%d\n", n, p);
        if (array[n-1] < array[p]) {
            return max_position(n-1, array);  /* @ 後問で書き換え */
        } else {
            return max_position(p, array);
        }
    }
    return n;  // returnにスコープ外の変数を含めない
}

