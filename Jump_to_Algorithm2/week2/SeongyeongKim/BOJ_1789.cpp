#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0); 

	long long S;
	cin >> S;

	long long N = 1, cnt = 0;

	//�ڿ��� ���� S�� �ѱ� ������ N�� ��� ����
	while (S >= 0) {
		S -= N;
		N++;
		cnt++;
	}

	//�ڿ��� ���� S�� �ѱ�Ƿ� cnt �ϳ� ����� ��
	cout << --cnt;

	return 0;
}