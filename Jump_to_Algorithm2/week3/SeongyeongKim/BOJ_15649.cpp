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

			//false�� �����ؾ� leve �� �ܰ��(level-1, level-1, ..)�� �� ���� Ž��(�湮)�� �� �ֱ� ����
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