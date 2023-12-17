#include <bits/stdc++.h>
using namespace std;

int nodeMap[1001][1001];
int visited[1001];

int n, m, v;

void dfs(int start) {
	cout << start << ' ';

	//���� ����ŭ Ž�� ����
	for (int i = 1; i <= n; i++) {
		//����1) start ������ i ������ ����Ǿ��ִ���
		//����2) i ������ �湮���� �ִ���
		if (nodeMap[start][i] && !visited[i]) {
			//���� ������ �����Ѵٸ� i�� �湮�� ���� �ٲٰ�,
			visited[i] = 1;
			//i�� dfs�� Ž��(���) 
			//���� i �������� ���̻� Ž���� �Ұ����Ҷ����� ����
			dfs(i);
		}
	}
}

void bfs(int start) {
	queue<int> q;

	//bfs�� queue�� ���
	q.push(start);

	//q�ȿ� Ž���� ���� ���������� ����
	while (!q.empty()) {
		int idx = q.front();
		q.pop();

		cout << idx << ' ';

		//dfs�� ������ �����ѵ�, �ڷᱸ���� queue�� �������� ����
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