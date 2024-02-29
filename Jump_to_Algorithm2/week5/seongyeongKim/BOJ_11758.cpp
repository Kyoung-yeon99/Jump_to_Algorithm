//CCW 알고리즘
//참고) https://snowfleur.tistory.com/98
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int x1, x2, x3, y1, y2, y3;

	cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

	int ans = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1);

	if (ans > 0) cout << 1;
	else if (ans < 0)cout << -1;
	else cout << 0;

	return 0;
}
