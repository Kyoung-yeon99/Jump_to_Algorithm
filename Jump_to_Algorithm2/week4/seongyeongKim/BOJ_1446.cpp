#include <bits/stdc++.h>
using namespace std;

//�� i�� ���� �ּ� ���(DP)
int minDis[10001]; 
//index�� ������ ���� ��ġ <int, int>�� ������ ���� ��ġ�� ����
vector<pair<int, int>> v[10001]; 

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int n, d;

	cin >> n >> d;

	int Start, End, Dis;
	for (int i = 0; i < n; i++) {
		cin >> Start >> End >> Dis;

		//������ �������� d�� ����ų� �������� ���̰� (������-����) ���̺��� ũ�� v�� �߰����� ����
		if (End > d || End - Start < Dis) continue; 
		v[End].push_back({ Start, Dis });
	}

	//minDis dp ���̺��� �����ϱ� ���� �ִ����� �ʱ�ȭ
	fill(minDis, minDis + 10001, 987654321);

	minDis[0] = 0;

	//DP minDis ä���
	for (int i = 1; i <= d; i++) {
		//�켱, minDis �� ������ 1�� ���ϸ� �ּ� �Ÿ��� �Է�
		minDis[i] = minDis[i - 1] + 1;

		//i�� ���� �������� �ִ��� Ȯ��
		for (int j = 0; j < v[i].size(); j++) {
			//minDis[v[i][j].first] - ������ ��������� ���� �ּ� �Ÿ�
			//v[i][j].second - ������ �Ÿ�

			//���� �� ����� �հ� minDis[i]�� �ּ� ���� minDis[i]�� ����
			minDis[i] = min(minDis[i], minDis[v[i][j].first] + v[i][j].second);
		}
	}

	cout << minDis[d];

	return 0;
}