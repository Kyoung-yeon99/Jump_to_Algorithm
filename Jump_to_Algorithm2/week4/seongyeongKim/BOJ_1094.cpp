#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int x, len = 64, temp = 64;
	cin >> x;

	int cnt = 1;
	while (len>x) {
		//������ �ִ� ���� ������ ���� ª�� ���� �������� �ڸ�
		temp /= 2;

		//������ �ڸ� ������� �ϳ��� ���� ���� x���� ũ�ų� ������ ����
		if (len - temp >= x)
			len -= temp;
		else
			cnt++;
	}

	cout << cnt;

	return 0;
}