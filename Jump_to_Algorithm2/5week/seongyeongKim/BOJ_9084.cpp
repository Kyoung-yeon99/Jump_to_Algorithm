/*
sp ��ȭ�� ǥ : https://fieldanimal.tistory.com/46
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int t;
	cin >> t;

	while (t--) {
		int n, m;
		cin >> n;

		int coins[20];
		for (int i = 0; i < n; i++)
			cin >> coins[i];

		cin >> m;

		int dp[10001]; //index �ݾ��� ���� �� �ִ� ����� 

		//dp init
		fill(dp, dp + 10001, 0);
		dp[0] = 1;

		//dp ��ȭ��
		//������ ���� - ù��° for��
		for (int i = 0; i < n; i++) {
			//���� �ݾ����� m�� �ѱ���� dp ä���
			for (int j = coins[i]; j <= m; ++j) {
				//���� j�� �ε������� ���� ���� �� ���� dp �� ����
				dp[j] += dp[j - coins[i]];
			}
		}

		cout << dp[m] << '\n';
	}

	return 0;
}