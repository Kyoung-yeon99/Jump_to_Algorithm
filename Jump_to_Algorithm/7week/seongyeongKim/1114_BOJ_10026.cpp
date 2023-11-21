#include <bits/stdc++.h>
using namespace std;

int n;
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0,0,-1,1 };
char _map[100][100];

int normal() {
	int cnt = 0;
	bool visited[100][100] = { false, };

	queue <pair<int, int>> q;
	//for문으로 전체 탐색 진행해야 되는 코드 짜기
	//bfs 탐색이 끝나면 다음칸 진행해야 하니까
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visited[i][j]) {
				cnt++;
				q.push({ i,j });
				visited[i][j] = true;
				char color = _map[i][j];

				while (!q.empty()) {
					int x = q.front().first;
					int y = q.front().second;
					q.pop();

					for (int i = 0; i < 4; i++) {
						int nx = x + dx[i];
						int ny = y + dy[i];

						if (nx < 0 || nx >= n || ny < 0 || ny >=
							n)
							continue;

						if (visited[nx][ny])
							continue;

						if (color == _map[nx][ny]) {
							q.push({ nx, ny });
							visited[nx][ny] = true;
						}
					}
				}
			}
		}
	}
	return cnt;
}

int unormal() {
	int cnt = 0;
	bool visited[100][100] = { false, };

	queue <pair<int, int>> q;
	//for문으로 전체 탐색 진행해야 되는 코드 짜기
	//bfs 탐색이 끝나면 다음칸 진행해야 하니까
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visited[i][j]) {
				cnt++;
				q.push({ i,j });
				visited[i][j] = true;
				char color = _map[i][j];

				while (!q.empty()) {
					int x = q.front().first;
					int y = q.front().second;
					q.pop();

					for (int i = 0; i < 4; i++) {
						int nx = x + dx[i];
						int ny = y + dy[i];

						if (nx < 0 || nx >= n || ny < 0 || ny >= n)
							continue;

						if (visited[nx][ny])
							continue;

						if (color == 'R' || color == 'G') {
							if (_map[nx][ny] != 'B') {
								q.push({ nx, ny });
								visited[nx][ny] = true;
							}
						}
						else {
							if (_map[nx][ny] == 'B') {
								q.push({ nx, ny });
								visited[nx][ny] = true;
							}
						}
					}
				}
			}
		}
	}
	return cnt;
}

int main() {
	//ios::sync_with_stdio(0);
	//cin.tie(0); cout.tie(0);

	char c;

	cin >> n;
	cin.ignore();
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%1c", &_map[i][j]);
		}
		cin.ignore();
	}

	cout << normal() << " " << unormal();

	return 0;
}
