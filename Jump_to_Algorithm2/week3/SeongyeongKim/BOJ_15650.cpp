#include <bits/stdc++.h>
using namespace std;

int N, M;
int arr[8];
bool visited[9];

void backtracking(int n, int level) {
	if (level == M) {
		for (int i = 0; i < M; i++)
			cout << arr[i] << ' ';
		cout << '\n';
	}

	//수열이 오름차순이어야 하므로 i는 n부터 시작
	for (int i = n; i <= N; i++) {
		if (!visited[i]) {
			arr[level] = i;
			visited[i] = true;
			backtracking(i + 1, level + 1);
			visited[i] = false;
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0); 

	cin >> N >> M;

	backtracking(1, 0);

	return 0;
}