//�ֵ� ���� ���� �𸣰�����..
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int t, l, n;
	cin >> t;

	while (t--) {
		//��� ���̵��� �� �������� �ִܽð��� ����ð� - �����ؾ� ��
		int minSec = 0, maxSec = 0;

		cin >> l >> n;
		int inputX;
		for (int i = 0; i < n; i++) {
			cin >> inputX;

			//�� ���� ���� �� �ּҰ� ���� �������� �ð�
			int tempMin = min(inputX, l - inputX);
			//��� ���̵��� �������� �ϴ� �ð��� ���ؾ��ϹǷ�
			//������ ���� �ּ� �ð��� ������� �ּ� �ð��� ū ������ minSec ����
			minSec = max(minSec, tempMin);

			//�� ���� ���� �� �ִ밡 ���� �������� �ð�
			int tempMax = max(inputX, l - inputX);
			maxSec = max(maxSec, tempMax);
		}

		cout << minSec << ' ' << maxSec << '\n';
	}

	return 0;
}