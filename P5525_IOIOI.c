#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int n, m, j, end;
    int i = 0, cnt = 0;
    char test[2] = {'I', 'O'};
    char * s;
    scanf("%d %d", &n, &m);
    scanf("%s", s);
    while (2 * n + 1 + i <= m) {
        if (s[i] == 'I') {
            j = i;
            end = 0;
            while (j < 2 * n + 1 + i){
                if (s[j] == test[(j - i) % 2]){
                    j ++;
                }
                else {
                    i = j;
                    end = 1;
                    break;
                }
            }
            if (!end) {
                cnt ++;
                i += 2;
            }
        }
        else {
            i ++;
        }
    }
    printf("%d", cnt);
    return 0;
}