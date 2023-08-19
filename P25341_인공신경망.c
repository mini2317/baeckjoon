#include <stdio.h>
typedef struct {
  int weight;
  int node;
} Edge;

int main() {
    int N, M, Q, C, temp, outputBias;
    scanf("%d %d %d", &N, &M, &Q);
    int inputWeight[2001][2001] = {0, };
    int inputBias[2001];
    int node[2001];
    int outputWeight[2001];
    int input[2001];
    int output;
    for (int i = 0; i < M; i++) {
        scanf("%d", &C);
        for (int j = 0; j < C; j++) scanf("%d", &node[j]);
        for (int j = 0; j < C; j++) {
            scanf("%d", &temp);
            inputWeight[node[j] - 1][i] = temp;
        }
        scanf("%d", &inputBias[i]);
    }
    for (int j = 0; j < M; j++) scanf("%d", outputWeight[j]);
    scanf("%d", &outputBias);
    for (int i = 0; i < Q; i++) {
        output = outputBias;
        int hidden[2001] = {0, };
        for (int j = 0; j < N; j++) {
            scanf("%d", &temp);
            for (int k = 0; k < M; k++) {
                hidden[k] += inputWeight[j][k] * temp;
            }
        }
        for (int j = 0; j < M; j++) output += (hidden[j] + inputBias[j]) * outputWeight[j];
        printf("%d\n", output);
    }
    return 0;
}
