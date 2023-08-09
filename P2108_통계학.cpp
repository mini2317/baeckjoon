#include <iostream>
#include <vector>
#include<cmath>

#define ZERO_IDX 4000
#define MIN -4001
#define MAX 4001

using namespace std;

int main()
{
    int N, best, sum = 0;
    int min = MAX;
    int max = MIN;
    int count[8001] = {0};
    int elite[2] = {MIN, MIN};
    vector<int> input;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        int newInput;
        cin >> newInput;
        sum += newInput;
        if (min > newInput) min = newInput;
        if (max < newInput) max = newInput;
        int find = i / 2;
        int divide = 2;
        int sizeOfInput = i;
        for (int j = 0; j < sizeOfInput; j++)
        {
            divide *= 2;
            int move = sizeOfInput/divide;
            int isMoveZero = (move == 0);
            if (input[find] > newInput)
            {
                find -= move + isMoveZero;
                if (find < 0) find = 0;
            }
            else if (input[find] < newInput)
            {
                find += move + isMoveZero;
                if (find > sizeOfInput) find = sizeOfInput;
            }
            else
            {
                if (find == sizeOfInput) input.push_back(newInput);
                else input.insert(input.begin() + find, newInput);
                break;
            }
            if (isMoveZero)
            {
                if (find == sizeOfInput) input.push_back(newInput);
                else input.insert(input.begin() + find, newInput);
                break;
            }
            if (j == sizeOfInput - 1)input.push_back(newInput);
        }
        if (sizeOfInput == 0)
        {
            input.push_back(newInput);
        }
        sizeOfInput += 1;
        ++ count[sizeOfInput + ZERO_IDX];
        int nowCount = count[sizeOfInput + ZERO_IDX];
        if (nowCount > best)
        {
            elite[0] = newInput;
            best = nowCount;
        }
        else if (nowCount == best)
        {
            if (elite[0] > newInput)
            {
                elite[1] = elite[0];
                elite[0] = newInput;
            }
            else if (elite[1] == MIN) elite[1] = newInput;
            else if (elite[1] > newInput) elite[1] = newInput;
        }
    }
    cout << round(sum/N) << endl;
    cout << input[input.size()/2] << endl;
    if (elite[1] == MIN) cout << elite[0] << endl;
    else cout << elite[1] << endl;
    cout << max - min << endl;
    return 0;
}
