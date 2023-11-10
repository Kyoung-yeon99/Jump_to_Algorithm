#include <bits/stdc++.h>
using namespace std;

int mirro[100][100];

int dx[4] = { 0, 0,-1,1 };
int dy[4] = { -1, 1, 0, 0 };

int n, m;

void bfs(int inputX, int inputY) {
	queue<pair<int, int>> q;
	q.push({ inputX, inputY });

	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (0 <= nx && nx < n && 0 <= ny && ny < m) {
				if (mirro[nx][ny] == 1) {
					q.push({ nx, ny });
					mirro[nx][ny] = mirro[x][y] + 1;
				}
			}
		}
	}
}

int main() {
	string input;

	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> input;

		for (int j = 0; j < m; j++) {
			mirro[i][j] = input[j] - '0';
		}
	}

	bfs(0, 0);

	cout << mirro[n - 1][m - 1];

	return 0;
}