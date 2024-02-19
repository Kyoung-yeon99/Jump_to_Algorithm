/*
참고한 풀이 : https://hackids.tistory.com/109
참고했지만, 틀림
*/

#include <bits/stdc++.h>
using namespace std;

int _map[500][500];
int dp[500][500];
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };
int n, m;

int dfs(int y, int x) {
	if (y == m - 1 && x == n - 1)
		return 1;

	if (dp[y][x] == -1) {
		dp[y][x] = 0;
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (_map[ny][ny] != 0 && _map[y][x] > _map[ny][nx])
				dp[y][x] += dfs(ny, nx);
		}
	}

	return dp[y][x];
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	cin >> m >> n;

	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
			cin >> _map[i][j];

	memset(dp, -1, sizeof(dp));

	cout << dfs(0, 0);

	return 0;
}