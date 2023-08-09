#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void addItem(char** S, int size, char* x);
void removeItem(char** S, int size, char* x);
void checkItem(char** S, int size, char* x);
void toggleItem(char** S, int size, char* x);
void empty(char** S, int size);
void getSize(char** S, int size);
int isFull(char** S, int size);
int find(char** S, int size, char* x);
int getIndex(char** S, int size);

int sameStr(char * str1, char * str2) {
    while (*str1 != '\0' && *str2 != '\0') {
        if (*str1 != *str2) return 0;
        str1++;
        str2++;
    }
    return (*str1 == *str2);
}

char* input() {
    char* str = NULL;
    int size = 0;
    int capacity = 16;
    str = (char*)malloc(capacity * sizeof(char));
    if (str == NULL) {
        printf("메모리 할당 오류!\n");
        return NULL;
    }
    char one;
    scanf(" ");
    while (1) {
        scanf("%c", &one);
        if (one == '\n') break;
        str[size++] = one;
        if (size == capacity) {
            capacity *= 2;
            char* temp = NULL;
            temp = (char*)realloc(str, capacity * sizeof(char));
            if (temp == NULL) {
                printf("메모리 할당 오류!\n");
                free(str);
                return NULL;
            }
            str = temp;
        }
    }
    str[size] = '\0';
    return str;
}

int main()
{
    char** S = NULL;
    char comm[6];
    int size;
    printf("집합 크기 설정 : ");
    scanf("%d", &size);
    S = (char**)malloc(sizeof(char*) * size);
    if (S == NULL) {
        printf("메모리 할당 오류!");
        return -1;
    }
    for (int i = 0; i < size; i++) S[i] = NULL;
    while (1) {
        printf("연산을 선택하세요 : ");
        scanf("%s", comm);
        if (sameStr(comm, "add")) {
            char* x = input();
            addItem(S, size, x);
        }
        else if (sameStr(comm, "remove")) {
            char* x = input();
            removeItem(S, size, x);
        }
        else if (sameStr(comm, "check")) {
            char* x = input();
            checkItem(S, size, x);
        }
        else if (sameStr(comm, "toggle")) {
            char* x = input();
            toggleItem(S, size, x);
        }
        else if (sameStr(comm, "empty")) {
            empty(S, size);
        }
        else if (sameStr(comm, "Size")) {
            getSize(S, size);
        }
        printf("집합 : { ");
        for (int i = 0; i < size; i++) {
            if (S[i] != NULL) printf("%s ", S[i]);
        }
        printf("}\n");
    }
    for (int i = 0; i < size; i++) {
        free(S[i]);
    }
    free(S);
    return 0;
}

void addItem(char** S, int size, char* x) {
    int isInclude = find(S, size, x);
    if (!isFull(S, size)) {
        if (isInclude == -1) {
            int index = getIndex(S, size);
            S[index] = x;
        }
    }
    else {
        printf("집합이 모두 찬 상태에서 추가할 수 없습니다.\n");
        return;
    }
}

void removeItem(char** S, int size, char* x) {
    int index = find(S, size, x);
    if (index != -1) {
        free(S[index]);
        S[index] = NULL;
    }
}

void checkItem(char** S, int size, char* x) {
    int index = find(S, size, x);
    if (index != -1) printf("1\n");
    else printf("0\n");
}

void toggleItem(char** S, int size, char* x) {
    int index = find(S, size, x);
    if (index != -1) removeItem(S, size, x);
    else addItem(S, size, x);
}

void empty(char** S, int size) {
    for (int i = 0; i < size; i++) {
        if (S[i] != NULL) S[i] = NULL;
    }
}

void getSize(char** S, int size) {
    int rst = 0;
    for (int i = 0; i < size; i++) {
        rst += (S[i] != NULL);
    }
    printf("집합 크기 : %d\n",rst);
}

int isFull(char** S, int size) {
    return (getIndex(S, size) == -1);
}

int find(char** S, int size, char* x) {
    for (int i = 0; i < size; i++) {
        if (S[i] != NULL && sameStr(S[i], x) == 0)
            return i;
    }
    return -1;
}

int getIndex(char** S, int size) {
    for (int i = 0; i < size; i++) {
        if (S[i] == NULL)
            return i;
    }
    return -1;
}