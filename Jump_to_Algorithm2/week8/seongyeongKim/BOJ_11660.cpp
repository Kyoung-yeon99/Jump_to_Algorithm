/*
* refer : https://donggoolosori.github.io/2020/10/13/boj-11660/
*/
#include <bits/stdc++.h>
using namespace std;

int N, M;
int _map[1025][1025];
int dp[1025][1025];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> M;

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cin >> _map[i][j];
			dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + _map[i][j];
		}
	}

	int x1, y1, x2, y2;
	for (int t = 0; t < M; t++) {
		cin >> x1 >> y1 >> x2 >> y2;
		cout << dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1] << '\n';
	}


	return 0;
}