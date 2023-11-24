#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int N, M;

    cin >> N >> M;
    string dna[1000];

    string str;
    for (int i = 0; i < N; i++) {
        cin >> dna[i];
    }

    string result = "";
    int resultCnt = 0;

    int aCnt, tCnt, gCnt, cCnt;
    //각 문자의 동일 자릿수를 탐색하면서
    //가장 많은 문자인 것을 선정함
    for (int i = 0; i < M; i++) {
        aCnt = 0; tCnt = 0; gCnt = 0; cCnt = 0;

        for (int j = 0; j < N; j++) {
            if (dna[j][i] == 'A')
                aCnt++;
            else if (dna[j][i] == 'T')
                tCnt++;
            else if (dna[j][i] == 'G')
                gCnt++;
            else
                cCnt++;
        }

        int maxValue = max({ aCnt, tCnt, gCnt, cCnt });
        resultCnt += (N - maxValue);

        if (aCnt == maxValue)
            result += "A";
        else if (cCnt == maxValue)
            result += "C";
        else if (gCnt == maxValue)
            result += "G";
        else
            result += "T";
    }

    cout << result << "\n" << resultCnt;

    return 0;
}