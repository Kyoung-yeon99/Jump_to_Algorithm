#include <bits/stdc++.h>
using namespace std;

int maxDepth = 0;
int N;
int _map[100][100];
int result = 0;
int checkMap[100][100];

int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

void bfs(int ix, int iy) {
    queue<pair<int, int>> q;
    q.push({ ix, iy });

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N)
                continue;
            if (checkMap[nx][ny] == 0) {
                q.push({ nx, ny });
                checkMap[nx][ny] = 1;
            }
        }
    }
}

int main()
{
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> _map[i][j];
            if (_map[i][j] > maxDepth)
                maxDepth = _map[i][j];
        }
    }

    for (int i = 0; i <= maxDepth; i++) {
        int cnt = 0;
        for (int a = 0; a < N; a++)
            for (int b = 0; b < N; b++)
                checkMap[a][b] = 0;

        for (int a = 0; a < N; a++)
            for (int b = 0; b < N; b++)
                if (_map[a][b] <= i)
                    checkMap[a][b] = 1;

        for (int a = 0; a < N; a++) {
            for (int b = 0; b < N; b++) {
                if (checkMap[a][b] == 0) {
                    bfs(a, b);
                    cnt++;
                }
            }
        }

        if (cnt > result) {
            result = cnt;
        }
    }

    cout << result;

    return 0;
}
