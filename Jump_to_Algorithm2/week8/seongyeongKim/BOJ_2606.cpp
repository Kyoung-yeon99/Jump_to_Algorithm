/*
* similar problem : BOJ 11403
* https://www.acmicpc.net/problem/11403
*/

#include <bits/stdc++.h>
using namespace std;

int cnt = 0;
bool visited[101]; //�ش� ��� �湮 ���� ǥ��
vector<int> v[101]; //�ε��� ���� ����� ����

//����� ��� ������ Ž����
void dfs(int n) {
	visited[n] = true;
	cnt++;
	//n ���� ����� ��� ���� Ž��
	for (int i = 0; i < v[n].size(); i++) {
		if (visited[v[n][i]])
			continue;
		//�湮���� �ʾ����� dfs Ž��
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
		//��� ������ ��������� ó���ؾ� ��
		v[a].push_back(b);
		v[b].push_back(a);
	}

	dfs(1);

	cout << --cnt;

	return 0;
}