#include <bits/stdc++.h>
using namespace std;

int n, p1, p2, m;
vector<int> v[100];
bool visited[100]; //�� ��� Ž���ߴ��� Ȯ��

//int cnt = 0; //�������� ������ ����� count X
bool canCalc = false;

//cnt�� ���� �����ؾ� ��
void dfs(int p, int cnt) {
	//�̼� ����ؾ� �ϴ� ��� ã���� Ž�� ����
	if (p == p2) {
		cout << cnt;
		canCalc = true;
		return;
	}
	
	//p�� ����� ��� ��� Ž��
	for (int i = 0; i < v[p].size(); i++) {
		//����� ����� �̹� Ž���� ������� Ȯ��
		if (visited[v[p][i]])
			continue;
		
		//�湮 ó���ϰ� Ž�� ����
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