#include <bits/stdc++.h>
using namespace std;

int N;
char _map[11][11];
char inp[11][11];
char out[11][11];
int dx[8] = { 0, 0, -1, 1, -1, -1, 1, 1 };   //��, ��, ��, ��, ���� ��, ���� �Ʒ�, ������ ��, ������ �Ʒ�
int dy[8] = { -1, 1, 0, 0, -1, 1, -1, 1 };


int dfs(int x, int y, int cnt) {
    for (int i = 0; i < 8; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
            if (_map[nx][ny] == '*') cnt++;
        }
    }
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    bool flag = false;  //���ڸ� ��Ҵ��� �ȹ�Ҵ��� Ȯ��
    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int k = 0; k < N; k++) {
            cin >> _map[i][k];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int k = 0; k < N; k++) {
            cin >> inp[i][k];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int k = 0; k < N; k++) {
            if (inp[i][k] == 'x') {
                int cnt = dfs(i, k, 0);
                out[i][k] = cnt + '0';
                if (_map[i][k] == '*') flag = true;    // ���ڸ� ����.
            }
            else if (inp[i][k] == '.') out[i][k] = '.';

        }
    }

    if (flag) {
        for (int i = 0; i < N; i++) {
            for (int k = 0; k < N; k++) {
                if (_map[i][k] == '*') out[i][k] = '*';
            }
        }
    }

    for (int i = 0; i < N; i++) {
        for (int k = 0; k < N; k++) {
            cout << out[i][k];
        }
        cout << '\n';
    }


}