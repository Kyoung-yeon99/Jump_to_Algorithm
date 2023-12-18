/*
참고한 풀이
https://gimkuku0708.tistory.com/3
*/

#include <bits/stdc++.h>
using namespace std;

int N, S;
vector<int> v;
int cnt = 0;

void dfs(int level, int value) {
	if (level == N)
		return;
	if (value + v[level] == S) cnt++;

	dfs(level + 1, value);
	dfs(level + 1, value + v[level]);
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> S;

	int inputNum;
	for (int i = 0; i < N; i++) {
		cin >> inputNum;
		v.push_back(inputNum);
	}

	dfs(0, 0);
	cout << cnt;

	return 0;
}