#include <bits/stdc++.h>
using namespace std;

int n, p1, p2, m;
vector<int> v[100];
bool visited[100]; //이 사람 탐색했는지 확인

//int cnt = 0; //전역으로 넣으면 제대로 count X
bool canCalc = false;

//cnt의 상태 전달해야 함
void dfs(int p, int cnt) {
	//촌수 계산해야 하는 사람 찾으면 탐색 종료
	if (p == p2) {
		cout << cnt;
		canCalc = true;
		return;
	}
	
	//p와 연결된 모든 사람 탐색
	for (int i = 0; i < v[p].size(); i++) {
		//연결된 사람이 이미 탐색된 사람인지 확인
		if (visited[v[p][i]])
			continue;
		
		//방문 처리하고 탐색 시작
		visited[v[p][i]] = true;
		dfs(v[p][i], cnt+1);
	}
	return;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> p1 >> p2 >> m;

	int x, y;
	for (int i = 0; i < m; i++) {
		cin >> x >> y;
		v[x].push_back(y);
		v[y].push_back(x);
	}

	dfs(p1, 0);
	if (!canCalc)
		cout << "-1";

	return 0;
}