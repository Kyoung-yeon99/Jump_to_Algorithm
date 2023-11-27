#include <bits/stdc++.h>
using namespace std;

int N, M;
int startCity, endCity;

int _map[1000][1000];
bool visited[1000];
int result = 987654321;

void dfs(int city, int cost) {
	if (city == endCity) {
		if (cost < result) {
			result = cost;
		}
		return;
	}

	visited[city] = true;

	for (int i = 0; i < M; i++) {
		if (_map[city][i] && !visited[i]) {
			dfs(i, cost + _map[city][i]);
		}
	}

	visited[city] = false;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0); 

	cin >> N >> M;

	int s, e, cost;
	for (int i = 0; i < M; i++) {
		cin >> s >> e >> cost;
		_map[s][e] = cost;
	}

	cin >> startCity >> endCity;

	dfs(startCity, 0);

	cout << result;

	return 0;
}