#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	string s;
	cin >> s;

	int zeroCnt = 0, oneCnt = 0;

	char crit = s[0];
	if (s[0] == '0')
		zeroCnt++;
	else
		oneCnt++;

	for (int i = 1; i < s.length(); i++) {
		if (crit != s[i]) {
			if (s[i] == '0')
				zeroCnt++;
			else
				oneCnt++;
			crit = s[i];
		}
	}

	cout << min(zeroCnt, oneCnt);

	return 0;
}