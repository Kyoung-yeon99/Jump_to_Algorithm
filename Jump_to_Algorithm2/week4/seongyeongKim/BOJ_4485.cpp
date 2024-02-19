#include <bits/stdc++.h>
using namespace std;

int _map[126][126];
int minMap[126][126];
int n;
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

void init() {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			minMap[i][j] = 987654321;

	minMap[0][0] = _map[0][0];
}

void bfs() {
	init();

	queue<pair<int, int>> q;
	q.push({ 0, 0 });

	int x, y;
	while (!q.empty()) {
		x = q.front().first;
		y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || nx >= n || ny < 0 || ny >= n)
				continue;

			//���� ��ǥ�� �Ÿ��� ���� ��ǥ�� ���� ������ ����
			//������ �湮�� ��ǥ�� �Ÿ����� ���� ��� �����ϰ� queue�� �־� ��� Ž��
			if (minMap[x][y] + _map[nx][ny] >= minMap[nx][ny])
				continue;

			minMap[nx][ny] = minMap[x][y] + _map[nx][ny];
			q.push({ nx, ny });
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int gameCnt = 0;
	while (true) {
		cin >> n;

		if (n == 0)
			break;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> _map[i][j];
			}
		}

		bfs();

		cout << "Problem " << ++gameCnt << ": " << minMap[n - 1][n - 1] << '\n';
	}

	return 0;
}