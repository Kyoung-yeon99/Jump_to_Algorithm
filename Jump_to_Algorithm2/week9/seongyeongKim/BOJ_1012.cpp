#include <bits/stdc++.h>
using namespace std;

int N, M, K;
bool _map[50][50];
int cnt = 0;

int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

void bfs(int ix, int iy) {
	queue<pair<int, int>> q;
	q.push({ ix, iy });
	_map[ix][iy] = false;

	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || nx >= N || ny < 0 || ny >= M)
				continue;
			if (_map[nx][ny]) {
				q.push({ nx, ny });
				_map[nx][ny] = false;
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int t;
	cin >> t;

	int x, y;

	while (t--) {
		cin >> M >> N >> K;

		//init
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				_map[i][j] = false;
		cnt = 0;

		//input info
		for (int i = 0; i < K; i++) {
			cin >> y >> x;
			_map[x][y] = true;
		}

		//search
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (_map[i][j]) {
					bfs(i, j);
					cnt++;
				}
			}
		}

		cout << cnt << '\n';
	}


	return 0;
}