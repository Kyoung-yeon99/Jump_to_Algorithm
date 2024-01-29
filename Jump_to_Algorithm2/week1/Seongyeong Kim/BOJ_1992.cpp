#include <bits/stdc++.h>
using namespace std;

int N;
int arr[64][64];

void recur(int x, int y, int n) {
	int crit = arr[x][y];

	for (int i = x; i < x + n; i++) {
		for (int j = y; j < y + n; j++) {
			if (crit != arr[i][j]) {
				cout << '(';
				recur(x, y, n / 2);
				recur(x, y + n / 2, n / 2);
				recur(x + n / 2, y, n / 2);
				recur(x + n / 2, y + n / 2, n / 2);
				cout << ')';
				return; //분할 정복 종료조건 반드시 추가!
			}
		}
	}

	cout << crit;
	return;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N;
	string str;
	for (int i = 0; i < N; i++) {
		cin >> str;
		for (int j = 0; j < N; j++) {
			arr[i][j] = str[j] - '0';
		}
	}

	recur(0, 0, N);


	return 0;
}