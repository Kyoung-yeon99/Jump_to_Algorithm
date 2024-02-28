/*
sp 점화식 표 : https://fieldanimal.tistory.com/46
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

		int dp[10001]; //index 금액을 만들 수 있는 경우의 

		//dp init
		fill(dp, dp + 10001, 0);
		dp[0] = 1;

		//dp 점화식
		//동전의 개수 - 첫번째 for문
		for (int i = 0; i < n; i++) {
			//동전 금액으로 m을 넘기까지 dp 채우기
			for (int j = coins[i]; j <= m; ++j) {
				//현재 j의 인덱스에서 동전 값을 뺀 곳의 dp 값 더함
				dp[j] += dp[j - coins[i]];
			}
		}

		cout << dp[m] << '\n';
	}

	return 0;
}