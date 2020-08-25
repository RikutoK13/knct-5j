#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TRUE 1
#define FALSE -1
#define MAP_SIZE 99

int g_even_num = TRUE;  // TRUEで奇数ターン(1ターン目からカウント)

typedef struct {
    int map[MAP_SIZE];  // 処理の値が入る(proc_squaresで処理)
    int person[4];  // 座標が入る
} _objects;

void settings();
void init_objects(_objects *obs);
void update_even_num();
int proc_dice();
int proc_squares();

int main(void) {
    _objects _obs;
    init_objects(&_obs);

    while(1) {
        printf("%d\n", _obs.map[4]);
        update_even_num();
        return 0;
    }
    return 0;
}

void settings() {
    printf("初期設定で開始?\n");
    printf("初期設定:\n プレイヤー数:");
    // yesでオブジェクト書き換え,noで初期設定のまま開始
}

void init_objects(_objects *obs) {
    srand(1);
    for(int i=0; i < MAP_SIZE; i++) {
        obs->map[i] = (rand() % 6) + 1;
    }
    printf("%d\n", obs->map[4]);
    printf("ok\n");

}

void update_even_num() {
    // 奇数ターン:TRUE,偶数ターン:FALSE
    if(g_even_num == TRUE) g_even_num = FALSE;
    else if(g_even_num == FALSE) g_even_num = TRUE;
}

int proc_dice() {
    // サイコロを振る.奇数ターンで2回,偶数ターンで1回.偶数ターンは-1をかけて返す
}

