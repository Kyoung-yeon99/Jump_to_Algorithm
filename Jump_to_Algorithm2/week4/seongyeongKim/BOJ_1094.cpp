#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int x, len = 64, temp = 64;
	cin >> x;

	int cnt = 1;
	while (len>x) {
		//가지고 있는 막대 길이중 가장 짧은 것을 절반으로 자름
		temp /= 2;

		//위에서 자른 막대길이 하나를 버린 것이 x보다 크거나 같으면 버림
		if (len - temp >= x)
			len -= temp;
		else
			cnt++;
	}

	cout << cnt;

	return 0;
}