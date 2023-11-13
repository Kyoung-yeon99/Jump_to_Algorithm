#include <bits/stdc++.h>
using namespace std;

int m, n;
int dx[4] = { 0,0,-1, 1 };
int dy[4] = { -1, 1, 0, 0 };
queue <pair<int, int>> q;
int graph[1000][1000];

int main() {

	cin >> n >> m;

	//입력
	int yetTomato = 0;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			cin >> graph[i][j];
			if (graph[i][j] == 1) {
				q.push({ i, j });
			}
			//안익을 토마토가 없는지 확인
			//yetTomato가 그대로 0이면 0을 출력하면 됨
			if (graph[i][j] == 0) {
				yetTomato++;
			}
		}
	}

	if (yetTomato == 0) {
		cout << "0\n";
		return 0;
	}

	//BFS 진행
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (0 > nx || nx >= m || 0 > ny || ny >= n)
				continue;

			if (graph[nx][ny] == 0) {
				graph[nx][ny] = graph[x][y] + 1;
				q.push({ nx, ny });
			}
		}
	}

	//날짜 확인
	int maxDay = 0;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (graph[i][j] == 0) {
				cout << "-1\n";
				return 0;
			}
			maxDay = maxDay < graph[i][j] ? graph[i][j] : maxDay;
		}
	}

	cout << maxDay - 1 << '\n';

	return 0;
}