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
			//s1�� ���ڿ� s2�� ���ڿ� ó������ ������ �ϳ��� ������ ��
			//�����ϸ� ���� �밢���� +1
			if (s1[i - 1] == s2[j - 1]) {
				dp[i][j] = dp[i - 1][j - 1] + 1;
			}
			//�ٸ��� ���ʰ� �� �߿� ū �� ��������
			else {
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
			}
		}
	}

	cout << dp[s1.length()][s2.length()];

	return 0;
}