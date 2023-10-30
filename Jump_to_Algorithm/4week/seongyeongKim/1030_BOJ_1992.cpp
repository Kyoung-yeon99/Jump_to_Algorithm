#include <bits/stdc++.h>
using namespace std;

int _map[64][64];
int n;

void search(int x, int y, int len) {
	int criti = _map[x][y];
	for (int i = 0; i < len; i++) {
		for (int j = 0; j < len; j++) {
			if (criti != _map[x + i][y + j]) {
				cout << '(';
				search(x, y, len / 2);
				search(x, y + len / 2, len / 2);
				search(x + len / 2, y, len / 2);
				search(x + len / 2, y + len / 2, len / 2);
				cout << ')';
				return;
			}
		}
	}
	cout << criti;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	string inputStr;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> inputStr;
		for (int j = 0; j < n; j++) {
			_map[i][j] = inputStr[j] - '0';
		}
	}

	search(0, 0, n);

	return 0;
}