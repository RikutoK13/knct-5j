//
// タスク
// マップの中身
// マップの表示
//

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TRUE 1
#define FALSE -1
#define MAP_SIZE 30  // マップサイズ
#define PEOPLE 1  // プレイヤー数

int g_even_num = TRUE;  // TRUEで奇数ターン(1ターン目からカウント)
int map[MAP_SIZE];  // 処理の値が入る(proc_squaresで処理)
int turn = 1;

typedef struct {
    int place;  // 座標が入る
    int money;  // 所持金が入る
    int goal_flag;  // ゴール判定
} _objects;

void settings();  // 設定管理
_objects init_objects(_objects obs);  // _objectsの初期化
void init_map();  // マップの初期化
void update_even_num();  // ターンの偶奇更新
_objects proc_dice(_objects obs);  // さいころで座標移動処理
_objects proc_squares(_objects obs);  // マップの内容処理
void display_map(_objects obs, int j);
void goal_effect(_objects obs);  // ゴール演出

int main() {
    _objects obs[PEOPLE];
    for (int i = 0; i < PEOPLE; i++) {
        obs[i] = init_objects(obs[i]);
    }
    settings();

    while (1) {
        int fin_flag = 0;  // 終了判定フラグ
        for (int k = 0; k < PEOPLE; k++) {
            if (obs[k].goal_flag == TRUE) fin_flag++;
        }
        if (fin_flag == PEOPLE) break;  // 全員ゴールで終了

        for (int j = 0; j < PEOPLE; j++) {
            // enterでさいころ
            int key_board = 0;
            while(getchar() != '\n');
            obs[j] = proc_dice(obs[j]);
            obs[j] = proc_squares(obs[j]);
            display_map(obs[j], j);
            // printf("%d\n", obs[j].place);
        }
        update_even_num();
    }
}

void settings() {

    srand((unsigned) time(NULL));
    init_map();

    printf("push Enter to roll dices\n");
    printf("\n");

}

_objects proc_dice(_objects obs) {
    // サイコロを振る.奇数ターンで2回,偶数ターンで1回.偶数ターンは-1をかけて戻る
    int dice_a = (rand() % 6) + 1;
    int dice_b = (rand() % 6) + 1;

    if (g_even_num == TRUE) {
        if (obs.place + dice_a + dice_b > MAP_SIZE) {
            obs.place = MAP_SIZE;  // ゴール
            obs.goal_flag = TRUE;
        } else {
            obs.place += dice_a + dice_b;  // 進む
         }
    } else {
        if (obs.place - dice_a < 0) {
            obs.place = 0;  // スタートに戻る
        } else {
            obs.place -= dice_a;  //　戻る
        }
    }
    return obs;
}

void display_map(_objects obs, int j) {

    printf("player%d ", j + 1);
    for (int i = 0; i < obs.place; i++) {
        printf(".");
    }
    printf("@\n");

}

_objects init_objects(_objects obs) {
    obs.place = 0;
    obs.money = 0;
    obs.goal_flag = FALSE;

    return obs;
}

void init_map() {
    for (int i = 0; i < MAP_SIZE; i++) {
        map[i] = 0;
    }

    map[MAP_SIZE - 1] = -1;  // ゴール
    map[1] = 8;  // ラッキーゴール
    map[MAP_SIZE - 2] = 19;  // スタートに戻る

    // プログラム下部に各処理記載
}

_objects proc_squares(_objects obs) {

    if (map[obs.place] == -1) obs.goal_flag = TRUE;
    if (map[obs.place] == 1) obs.place += 1;  // 1マス進む
    if (map[obs.place] == 2) obs.place += 2;  // 2マス進む
    if (map[obs.place] == 3) obs.place += 4;  // 3マス進む
    if (map[obs.place] == 8) obs.place = MAP_SIZE;  // ラッキーゴール
    if (map[obs.place] == 11) obs.place -= 1;  // 1マス戻る
    if (map[obs.place] == 12) obs.place -= 2;  // 2マス戻る
    if (map[obs.place] == 13) obs.place -= 3;  // 1マス戻る
    if (map[obs.place] == 21) obs.money += 100;  // 100ベリー獲得
    if (map[obs.place] == 22) obs.money += 200;  // 200ベリー獲得
    if (map[obs.place] == 23) obs.money += 300;  // 300ベリー獲得

    if (obs.place >= MAP_SIZE) obs.goal_flag = TRUE;
    return obs;
}

void update_even_num() {
    // 奇数ターン:TRUE,偶数ターン:FALSE
    if(g_even_num == TRUE) g_even_num = FALSE;
    else if(g_even_num == FALSE) g_even_num = TRUE;
    turn++;
}

/*
 * (map[] ==)
 * -1: ゴール
 * 0: 処理なし
 * 1: 1マス進む
 * 2: 2マス進む
 * 3: 3マス進む
 * 8: 100マス進む
 * 11: 1マス戻る
 * 12: 2マス戻る
 * 13: 3マス戻る
 * 19: スタートに戻る
 * 21: $100ゲット
 * 22: $200ゲット
 * 23: $300ゲット
 */

