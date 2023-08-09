#include <stdio.h>
#include <stdlib.h>

int max(int a, int b);
int length(int ** list, int size1, int size2);

typedef struct {
    char * str;
    int size;
} STRING;

STRING input() {
    STRING rst;
    rst.str = NULL;
    rst.size = 0;
    int capacity = 16;
    rst.str = (char*)malloc(capacity * sizeof(char));
    if (rst.str == NULL) {
        printf("메모리 할당 오류!\n");
        STRING error;
        error.str = "Error";
        error.size = -1;
        return error;
    }
    char one;
    while (1) {
        scanf("%c", &one);
        if (one == '\n') break;
        rst.str[rst.size++] = one;
        if (rst.size == capacity) {
            capacity *= 2;
            char* temp = NULL;
            temp = (char*)realloc(rst.str, capacity * sizeof(char));
            if (temp == NULL) {
                printf("메모리 할당 오류!\n");
                free(rst.str);
                STRING error;
                error.str = "Error";
                error.size = -1;
                return error;
            }
            rst.str = temp;
            free(temp);
        }
    }
    rst.str[rst.size] = '\0';
    return rst;
}

int sameStr(char * str1, char * str2) {
    while (*str1 != '\0' && *str2 != '\0') {
        if (*str1 != *str2) return 0;
        str1++;
        str2++;
    }
    return (*str1 == *str2);
}

int main() {
    while(1) {
        STRING str1, str2;
        int minLen = 0;
        str1 = input();
        if (sameStr(str1.str, "quit")) break;
        str2 = input();
        if (sameStr(str2.str, "quit")) break;
        if (str1.size < str2.size) minLen = str1.size;
        else minLen = str2.size;
        char * result = (char *) malloc(sizeof(char) * (minLen + 1));
        int ** dp = (int **) malloc(sizeof(int*) * (str1.size + 1));
        for (int i = 0; i < str1.size + 1; i++) dp[i] = (int *) malloc(sizeof(int) * (str2.size + 1));
        int i, j;
        for (i = 0; i < str1.size + 1; i++) {
            for (j = 0; j < str2.size + 1; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 0;
                }
                else if (str1.str[i - 1] == str2.str[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                }
                else {
                    dp[i][j] = 0;
                }
            }
    
        }
        int value = length(dp, str1.size, str2.size);
        int n = 0;
        for (int i = 0; i < str1.size + 1; i++) {
            for (int j = 0; j < str2.size + 1; j++) {
                if (dp[i][j] == value) {
                    for (int k = i - value; k < i; k++) {
                        result[n] = str1.str[k];
                        n++;
                    }
                    result[n] = '\0';
                }
            }
        }
        printf("%s / %d\n", result, value);
    }
    return 0;
}

int max(int a, int b) {
    if (a < b) {
        return b;
    }
    else {
        return a;
    }
}

int length(int ** list, int size1, int size2) {
    int len = 0;
    for (int i = 0; i < size1 + 1; i++) {
        for (int j = 0; j < size2 + 1; j++) {
            if (list[i][j] > len) {
                len = list[i][j];
            }
        }
    }
    return len;
}