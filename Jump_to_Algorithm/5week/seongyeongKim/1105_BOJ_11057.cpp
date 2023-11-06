/* 참고한 풀이
https://junbastick.tistory.com/3
*/

#include <bits/stdc++.h>
using namespace std;

#define MOD 10007
int N;
int dp[10];

int main()
{
	cin >> N;

	for (int i = 0; i < 10; i++)
		dp[i] = 1;
	
	for (int i = 0; i < N - 1; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			for (int k = j + 1; k < 10; k++)
			{
				dp[j] += dp[k];
			}
			dp[j] %= MOD;
		}
	}

	int result = 0;
	
	for (int i = 0; i < 10; i++)
		result += dp[i];
	
	cout << result % MOD;

	return 0;
}