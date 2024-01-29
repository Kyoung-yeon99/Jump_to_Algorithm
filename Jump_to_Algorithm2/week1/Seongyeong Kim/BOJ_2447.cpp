/*
������ Ǯ�� : https://winkite1226.tistory.com/119
*/

#include <bits/stdc++.h>
using namespace std;

void recur(int x, int y, int n) {
	//' '�� ��� ����
	if ((x / n) % 3 == 1 && (y / n) % 3 == 1) {
		cout << ' ';
	}
	else {
		//���� if ���ǿ� �ش� �ȵǸ�, �� ���� ���� n�� 3���� ���� ��� '*' ���
		if (n / 3 == 0) {
			cout << '*';
		}
		else {
			recur(x, y, n / 3);
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int N;
	cin >> N;

	//�� ��ǥ�� �ش��ؼ� �̰ʹ� '*'���� ' '������ ��ͷ� �˻��Ͽ� ����
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			recur(i, j, N);
		}
		cout << '\n';
	}

	return 0;
}