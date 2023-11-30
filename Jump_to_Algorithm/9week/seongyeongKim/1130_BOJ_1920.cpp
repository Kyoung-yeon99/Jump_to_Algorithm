#include <bits/stdc++.h>
using namespace std;

int n, m;
int num[100001];

void binarySearch(int findNum) {
	int low = 0;
	int high = n - 1;
	int mid;

	while (low <= high) {
		mid = (low + high) / 2;

		if (num[mid] == findNum) {
			cout << "1\n";
			return;
		}
		else if (num[mid] < findNum) low = mid + 1;
		else high = mid - 1;
	}
	cout << "0\n";
}

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int a;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a;
		num[i] = a;
	}

	sort(num, num + n);

	cin >> m;
	for (int i = 0; i < m; i++) {
		int b;
		cin >> b;
		binarySearch(b);
	}

	return 0;
}