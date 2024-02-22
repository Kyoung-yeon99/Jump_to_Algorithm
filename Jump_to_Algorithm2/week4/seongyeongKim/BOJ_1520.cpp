/*
참고한 풀이 : https://hackids.tistory.com/109
참고했지만, 틀림
*/

#include <bits/stdc++.h>
using namespace std;

int _map[500][500];
int dp[500][500]; //해당 좌표로 갈 수 있는 경로의 수
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };
int n, m;

int dfs(int y, int x) {
	if (y == m - 1 && x == n - 1)
		return 1;

	if (dp[y][x] == -1) {
		//0 : 해당 좌표로 갈 수 있는 경로 없음
		dp[y][x] = 0;
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			//다음에 잘 좌표가 내림차순이라면 dfs 또 진행
			if (_map[ny][nx] != 0 && _map[y][x] > _map[ny][nx])
				//다음에 갈 수 있는 모든 경로의 수들을 합한 것이 현재 좌표에서 갈 수 있는 경로의 수임
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

	//-1 : 방문하지 않았음을 의미
	memset(dp, -1, sizeof(dp));

	cout << dfs(0, 0);

	return 0;
}
