#include <bits/stdc++.h>
using namespace std;

vector<int> graph[1001];
bool visitied[1001];
int n, m;

void DFS(int nodeIdx) {
	visitied[nodeIdx] = true;

	//탐색을 진행하려는 노드와 연결된 노드들 모두 탐색 진행하여
	//연결 요소인지 확인
	for (int i = 0; i < graph[nodeIdx].size(); i++) {
		//방문하지 않은 노드만 탐색
		if (visitied[graph[nodeIdx][i]])
			continue;
		DFS(graph[nodeIdx][i]);
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int u, v;
	int result = 0;

	cin >> n >> m;

	while (m--) {
		cin >> u >> v;
		//무방향 그래프여서 양쪽으로 넣어줌
		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	//1부터 n까지의 노드를 방문하면서 
	//방문하지 않는 노드가 있다는 것은 연결이 끊겼다는 의미
	//만약에 1~n까지의 노드가 한번에 다 방문이 되어 있다는 것은, 한번에 연결이 다 되어 있다는 것
	for (int i = 1; i <= n; i++) {
		if (!visitied[i]) {
			DFS(i);
			result++;
		}
	}

	cout << result;

	return 0;

}