#include <stdio.h>
#include <stdlib.h>
int * sum(int * arr, int start, int end)
{
    int l = end - start + 1;
    if (l == 1){
        int * rst = (int *) malloc(sizeof(int)*2);
        rst[0] = arr[start];
        rst[1] = arr[start];
        return rst;
    }
    else if (l == 2){
        int * rst = (int *) malloc(sizeof(int)*2);
        rst[0] = arr[start] + arr[end];
        rst[1] = (arr[start] > arr[end]) ? arr[start] : arr[end];
        return rst;
    }
    else if (l == 3){
        int * rst = (int *) malloc(sizeof(int)*2);
        rst[0] = arr[start] + arr[end] + arr[start + 1];
        rst[1] = (arr[start] > arr[end]) ? arr[start] : arr[end];
        return rst;
    }
    else{
        int mid = l / 2;
        int * a = sum(arr, start, mid - 1);
        int * b = sum(arr, mid, end);
        int * rst = (int *) malloc(sizeof(int)*2);
        rst[0] = a[0] + b[0];
        rst[1] = (a[1] > b[1]) ? a[1] : b[1];
        return rst;
    }
}

int main()
{
    int T, N, k, i, j;
    scanf("%d", &T);
    for(int t = 0; t < T; t++){
        scanf("%d %d", &N, &k);
        int * ground = (int *) malloc(sizeof(int) * N);
        for(int i = 0; i < N; i++) scanf("%d", &ground[i]);
        for(int ii = 0; ii < k; ii++){
            scanf("%d %d", &i, &j);
            int * arr = (int *) malloc(sizeof(int) * (j - i + 1));
            for(int l = i - 1; l < j; l++) arr[l - i + 1] = ground[l];
            int * final = sum(arr, 0, j - i);
            printf("%d", final[1] * (j - i + 1) - final[0]);
        }
    }
    return 0;
}
