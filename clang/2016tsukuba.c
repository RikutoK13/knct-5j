//
// 2016年度 編入学試験 情報学群 問題3 情報基礎(1)
// 間違い等がありましたら,twitter @ripton0813までdmください
// githubは https://github.com/kr813 です.
// githubにメアド貼ってありますのでそちらでも構いません
// プログラム部分以外の解答は持ち合わせてません.過去問も同様です.
//
//  解答状況 (1):済み (2):木構造未作成
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#define N 10000
#define N 7  // めんどいから7で

struct node {
    int end_of_key;
    int value;
    struct node *next_char[26];
};

struct kv {
    char *key;
    int value;
};

struct kv kv_array[N];

struct node set_value(struct node *p);
int search_array(char *key);
int search_tree(struct node *root, char *key);
int numchar(char letter);


int main() {
    int ans_value_a = 0, ans_value_b = 0;
    struct node *p;
    p = malloc(sizeof(struct node));
    *p = set_value(&(*p));
    printf("%d\n", p->value);

    /*
    char a = 'z';
    printf("%d\n", numchar(a));  // num char確認用
     */
    ans_value_a = search_array("appear");
    printf("%d\n", ans_value_a);
    ans_value_b = search_tree(p, "ant");
    printf("%d\n", ans_value_b);

}

int search_array(char *key) {
    int start = 0;
    int end = N - 1;
    int middle;

    while (start <= end) {
        middle = (start + end) / 2;
        if (strcmp(kv_array[middle].key, key) == 0) {
            return kv_array[middle].value;
        } else if (strcmp(kv_array[middle].key, key) < 0){
            start = middle + 1;
        } else {
            end = middle - 1;  // 問1 (a) 二分探索の基礎
        }
    }
    return -1;  // 問1 (b) みつからなかった時-1を返すので
}

int search_tree(struct node *root, char *key) {
    int i, len;
    len = strlen(key);
    struct node *n = root;

    for (i = 0; i < len; i++) {
        if (n->next_char[numchar(key[i]) - 1] == NULL) {
            return -1;
        } else {
            //n = n->next_char[numchar(key[i]) - 1];  // 問3 (c) 次のノードへ
            n = n->next_char[0];
            printf("%d\n", n->end_of_key);
        }
    }

    if (n->end_of_key == 1) {
        return n->value;  // 問3 (d) 値を返す
    } else {
        return -1;
    }
}

struct node set_value(struct node *p) {
    kv_array[0].key = "ant";
    kv_array[0].value = 120;
    kv_array[1].key = "any";
    kv_array[1].value = 260;
    kv_array[2].key = "anyway";
    kv_array[2].value = 110;
    kv_array[3].key = "apart";
    kv_array[3].value = 380;
    kv_array[4].key = "appear";
    kv_array[4].value = 290;
    kv_array[5].key = "apple";
    kv_array[5].value = 190;
    kv_array[6].key = "bad";
    kv_array[6].value = 400;

    struct node *x = p;
    x = malloc(sizeof(struct node));
    x->value = 100;
    x->end_of_key = 0;
    x = malloc(sizeof(struct node));
    x->end_of_key = 0;
    x = x->next_char[numchar('n') - 1];
    x = malloc(sizeof(struct node));
    x->end_of_key = 0;
    x = x->next_char[numchar('t') - 1];
    x = malloc(sizeof(struct node));
    x->value = 120;
    x->end_of_key = 1;
    for (int i = 0;i < 26; i++) {
        x->next_char[i] = NULL;
    }
    /*
    for (int i = 0; i < 26; i++) {
        printf("ok\n");
        x->next_char[i] = NULL;
        printf("ok\n");
        x->next_char[i]->end_of_key = 1;
        printf("ok\n");
    }
    x = x->next_char[numchar('a') - 1];
    x->end_of_key = 0;
    for (int i = 0; i < 26; i++) {
        x->next_char[i] = NULL;
        x->next_char[i]->end_of_key = 1;
    }
    x = x->next_char[numchar('n') - 1];
    x->end_of_key = 0;
    for (int i = 0; i < 26; i++) {
        x->next_char[i] = NULL;
        x->next_char[i]->end_of_key = 1;
    }
    x = x->next_char[numchar('t') - 1];
    x->value = 120;
    x->end_of_key = 1;
    for (int i = 0; i < 26; i++) {
        x->next_char[i] = NULL;
        x->next_char[i]->end_of_key = 1;
    }
     */
    return **y;
}

int numchar(char letter) {
    int num = (int)letter + 0;
    num = num - 'a' + 1;
    return num;
}

