#include <bits/stdc++.h>
using namespace std;

int arr[10001];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int t, n;
	cin >> t;

	while (t--) {
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> arr[i];
		}

		//���� ���� ����
		sort(arr, arr + n);

		int result = 0;
		//���� �� ������ 2�� �볪������ ���� �� ���� ���̰� ū ��
		for (int i = 0; i < n-2; i++) {
			result = max(arr[i + 2] - arr[i], result);
		}

		cout << result << '\n';
	}

	return 0;
}