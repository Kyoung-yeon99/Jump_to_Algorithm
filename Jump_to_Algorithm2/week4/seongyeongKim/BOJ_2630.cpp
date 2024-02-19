#include <bits/stdc++.h>
using namespace std;

int N;
int arr[129][129];

int wCnt = 0, bCnt = 0;

void dc(int x, int y, int n) {
	int criti = arr[x][y];

	for (int i = x; i < x + n; i++) {
		for (int j = y; j < y + n; j++) {
			if (arr[i][j] != criti) {
				dc(x, y, n / 2);
				dc(x + n / 2, y, n / 2);
				dc(x, y + n / 2, n / 2);
				dc(x + n / 2, y + n / 2, n / 2);
				return;
			}
		}
	}

	if (criti == 0)
		wCnt++;
	else
		bCnt++;
	return;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> arr[i][j];
		}
	}

	dc(0, 0, N);

	cout << wCnt << '\n' << bCnt;

	return 0;
}