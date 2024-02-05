#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int num[9];

	int total = 0;
	
	for (int i = 0; i < 9; i++) {
		cin >> num[i];
		total += num[i];
	}

	int target = total - 100;

	int notIdx1, notIdx2;

	for (int i = 0; i < 8; i++) {
		for (int j = i+1; j < 9; j++) {
			if (num[i] + num[j] == target) {
				notIdx1 = i;
				notIdx2 = j;
				break;
			}
		}
	}

	for (int i = 0; i < 9; i++) {
		if (i == notIdx1 || i == notIdx2)
			continue;
		cout << num[i] << '\n';
	}

	return 0;
}