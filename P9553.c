#include <stdio.h>
#include <math.h>
int main() {
    int T, N, x1, y1, x2, y2;
    scanf("%d", &T);
    for (int testCase = 0; testCase < T; testCase++) {
        double sum = 0;
        scanf("%d", &N);
        for (int i = 0; i < N; i++) {
            scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
            double a = x1 * x1 + y1 * y1;
            double b = x2 * x2 + y2 * y2;
            double c = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
            sum += acos((a + b - c) / (2 * sqrt(a) * sqrt(b))) / (2 * 3.1415926535);
        }
        printf("%.5lf\n", sum);
    }
    return 0;
}
/*
2
2
1 5 3 3
3 5 6 2
8
3 0 0 3
0 3 -3 0
-3 0 0 -3
0 -3 3 0
3 3 -3 3
-3 3 -3 -3
-3 -3 3 -3
3 -3 3 3
*/
/*
0.20636
2.00000
*/