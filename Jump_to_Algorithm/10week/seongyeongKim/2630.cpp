#include <bits/stdc++.h>
using namespace std;

int white = 0, blue = 0;

int N;
int _map[128][128];

void divide(int x, int y, int len) {
    int flag = _map[x][y];

    for (int i = 0; i < len; i++) {
        for (int j = 0; j < len; j++) {
            if (flag != _map[x + i][y + j]) {
                divide(x, y, len / 2);
                divide(x + len / 2, y, len / 2);
                divide(x, y + len / 2, len / 2);
                divide(x + len / 2, y + len / 2, len / 2);
                return;
            }
        }
    }

    if (flag == 0)
        white++;
    else
        blue++;
}


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> _map[i][j];
        }
    }

    divide(0, 0, N);

    cout << white << '\n' << blue;

    return 0;
}