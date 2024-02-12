#include <bits/stdc++.h>
using namespace std;

int N, M;
bool visited[9];
int arr[9];

void backtracking(int level) {
	if (level == M) {
		for (int i = 0; i < M; i++)
			cout << arr[i] << ' ';
		cout << '\n';
	}

	for (int i = 1; i <= N; i++) {
		if (!visited[i]) {
			visited[i] = true;
			arr[level] = i;
			backtracking(level + 1);

			//false로 변경해야 leve 전 단계들(level-1, level-1, ..)이 이 곳을 탐색(방문)할 수 있기 때문
			visited[i] = false;
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	cin >> N >> M;

	backtracking(0);

	return 0;
}