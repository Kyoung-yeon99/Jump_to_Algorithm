#include <iostream>
#include <algorithm>
using namespace std;

int dp[1001][1001];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	string s1, s2;
	cin >> s1 >> s2;

	for (int i = 1; i <= s1.length(); i++) {
		for (int j = 1; j <= s2.length(); j++) {
			//s1의 문자와 s2의 문자열 처음부터 끝까지 하나씩 비교했을 때
			//동일하면 왼쪽 대각선에 +1
			if (s1[i - 1] == s2[j - 1]) {
				dp[i][j] = dp[i - 1][j - 1] + 1;
			}
			//다르면 왼쪽과 위 중에 큰 값 가져오기
			else {
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
			}
		}
	}

	cout << dp[s1.length()][s2.length()];

	return 0;
}