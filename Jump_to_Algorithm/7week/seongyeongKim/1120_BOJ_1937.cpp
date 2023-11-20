#include <bits/stdc++.h>
using namespace std;

int N;
int _map[500][500];
int dp[500][500]; //���� ĭ���� �̵��� �� �ִ� ��
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

int result = 0;

int dfs(int x, int y) {
	if (dp[x][y])
		return dp[x][y];

	dp[x][y] = 1;
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		//�̵��� ���� �볪���� �������� �� ����
		if (_map[nx][ny] > _map[x][y]) {
			dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1);
		}
	}

	return dp[x][y];
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N;
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> _map[i][j];
		}
	}

	//��� ��ǥ Ž��
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			result = max(result, dfs(i, j));
		}
	}

	cout << result;

	return 0;
}