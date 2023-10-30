#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int N, M;
int arr[8];
bool visited[9];

void dfs(int num, int level) {
    if (level == M) {
        for (int i = 0; i < M; i++)
            cout << arr[i] << ' ';
        cout << '\n';
    }

    for (int i = num; i <= N; i++) {
        if (!visited[i]) {
            arr[level] = i;
            visited[i] = true;
            dfs(i + 1, level + 1);
            visited[i] = false;
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N >> M;

    dfs(1, 0);

    return 0;
}
