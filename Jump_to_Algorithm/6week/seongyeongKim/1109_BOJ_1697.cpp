#include <bits/stdc++.h>
using namespace std;

int N, K;
int second = 0;
bool visited[100000];
int dx[2] = { -1, 1 };

void bfs(int start) {
	queue<pair<int, int>> q;
	q.push({ start, 0 });
	visited[start] = true;

	while (!q.empty()) {
		int x = q.front().first;
		int cnt = q.front().second;
		q.pop();

		if (x == K) {
			cout << cnt;
			break;
		}

		for (int i = 0; i < 3; i++) {
			int nx;
			if (i != 2) {
				nx = x + dx[i];
			}
			else {
				nx = x * 2;
			}

			if (nx < 0 || nx>100001)
				continue;
			if (visited[nx])
				continue;

			q.push({ nx, cnt + 1 });
			visited[nx] = true;
		}
	}
}

int main() {
	cin >> N >> K;

	bfs(N);

	return 0;
}