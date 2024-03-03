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
		//문제 풀이의 핵심은
		//출발점과 도착점이 각 n개의 원중 몇개 안에 속하는가 이다.
		//두 점이 하나의 원 안에 속하면 의미 없고,
		//하나의 원에 하나의 점이 속하는 경우에만 count
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