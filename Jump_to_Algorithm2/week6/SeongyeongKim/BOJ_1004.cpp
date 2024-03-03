#include <bits/stdc++.h>
//#include <iostream>
//#include <cmath>
using namespace std;

int x, y, x2, y2;

bool inCircle(int cx, int cy, int r) {
	if (pow(cx - x, 2) + pow(cy - y, 2) <= r * r && pow(cx - x2, 2) + pow(cy - y2, 2) <= r * r) return false;
	else if (pow(cx - x, 2) + pow(cy - y, 2) <= r * r) return true;
	else if (pow(cx - x2, 2) + pow(cy - y2, 2) <= r * r) return true;
	return false;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int t;
	cin >> t;

	int n, cx, cy, r;
	while (t--) {
		//���� Ǯ���� �ٽ���
		//������� �������� �� n���� ���� � �ȿ� ���ϴ°� �̴�.
		//�� ���� �ϳ��� �� �ȿ� ���ϸ� �ǹ� ����,
		//�ϳ��� ���� �ϳ��� ���� ���ϴ� ��쿡�� count
		cin >> x >> y >> x2 >> y2;
		cin >> n;

		int minCnt = 0;

		while (n--) {
			cin >> cx >> cy >> r;

			if (inCircle(cx, cy, r)) minCnt++;
		}

		cout << minCnt << '\n';

	}

	return 0;
}