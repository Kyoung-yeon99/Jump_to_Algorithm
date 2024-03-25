/*
* similar problem : BOJ 11403
* https://www.acmicpc.net/problem/11403
*/

#include <bits/stdc++.h>
using namespace std;

int cnt = 0;
bool visited[101]; //해당 노드 방문 여부 표시
vector<int> v[101]; //인덱스 노드와 연결된 노드들

//연결된 모든 노드들을 탐색함
void dfs(int n) {
	visited[n] = true;
	cnt++;
	//n 노드와 연결된 모든 노드들 탐색
	for (int i = 0; i < v[n].size(); i++) {
		if (visited[v[n][i]])
			continue;
		//방문하지 않았으면 dfs 탐색
		dfs(v[n][i]);
	}
	return;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int nodeCnt, lineCnt;

	cin >> nodeCnt >> lineCnt;

	int a, b;
	for (int i = 0; i < lineCnt; i++) {
		cin >> a >> b;
		//노드 연결을 양방향으로 처리해야 됨
		v[a].push_back(b);
		v[b].push_back(a);
	}

	dfs(1);

	cout << --cnt;

	return 0;
}