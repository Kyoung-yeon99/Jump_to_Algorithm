#include <bits/stdc++.h>
using namespace std;

int nodeMap[1001][1001];
int visited[1001];

int n, m, v;

void dfs(int start) {
	cout << start << ' ';

	//정점 수만큼 탐색 진행
	for (int i = 1; i <= n; i++) {
		//조건1) start 정점과 i 정점이 연결되어있는지
		//조건2) i 정점을 방문한적 있는지
		if (nodeMap[start][i] && !visited[i]) {
			//위에 조건을 충족한다면 i를 방문한 것을 바꾸고,
			visited[i] = 1;
			//i를 dfs로 탐색(재귀) 
			//따라서 i 정점에서 더이상 탐색이 불가능할때까지 진행
			dfs(i);
		}
	}
}

void bfs(int start) {
	queue<int> q;

	//bfs는 queue를 사용
	q.push(start);

	//q안에 탐색할 것이 없을때까지 진행
	while (!q.empty()) {
		int idx = q.front();
		q.pop();

		cout << idx << ' ';

		//dfs와 구현은 동일한데, 자료구조를 queue를 쓰느냐의 차이
		for (int i = 1; i <= n; i++) {
			if (nodeMap[idx][i] && !visited[i]) {
				q.push(i);
				visited[i] = 1;
			}
		}
	}
}

int main(void) {

	cin >> n >> m >> v;

	int nd1, nd2;

	for (int i = 0; i < m; i++) {
		cin >> nd1 >> nd2;
		nodeMap[nd1][nd2] = 1;
		nodeMap[nd2][nd1] = 1;
	}

	visited[v] = 1;
	dfs(v);

	cout << '\n';
	fill_n(visited, 1001, 0);
	visited[v] = 1;
	bfs(v);

	return 0;
}