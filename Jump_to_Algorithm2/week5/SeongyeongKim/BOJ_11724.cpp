#include <bits/stdc++.h>
using namespace std;

vector<int> graph[1001];
bool visitied[1001];
int n, m;

void DFS(int nodeIdx) {
	visitied[nodeIdx] = true;

	//Ž���� �����Ϸ��� ���� ����� ���� ��� Ž�� �����Ͽ�
	//���� ������� Ȯ��
	for (int i = 0; i < graph[nodeIdx].size(); i++) {
		//�湮���� ���� ��常 Ž��
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
		//������ �׷������� �������� �־���
		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	//1���� n������ ��带 �湮�ϸ鼭 
	//�湮���� �ʴ� ��尡 �ִٴ� ���� ������ ����ٴ� �ǹ�
	//���࿡ 1~n������ ��尡 �ѹ��� �� �湮�� �Ǿ� �ִٴ� ����, �ѹ��� ������ �� �Ǿ� �ִٴ� ��
	for (int i = 1; i <= n; i++) {
		if (!visitied[i]) {
			DFS(i);
			result++;
		}
	}

	cout << result;

	return 0;

}