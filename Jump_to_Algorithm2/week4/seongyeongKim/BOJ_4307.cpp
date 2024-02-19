//애드 훅이 뭔진 모르겠지만..
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int t, l, n;
	cin >> t;

	while (t--) {
		//모든 개미들이 다 떨어지는 최단시간과 최장시간 - 갱신해야 함
		int minSec = 0, maxSec = 0;

		cin >> l >> n;
		int inputX;
		for (int i = 0; i < n; i++) {
			cin >> inputX;

			//두 가지 방향 중 최소가 빨리 떨어지는 시간
			int tempMin = min(inputX, l - inputX);
			//모든 개미들이 떨어져야 하는 시간을 구해야하므로
			//위에서 구한 최소 시간과 현재까지 최소 시간중 큰 값으로 minSec 갱신
			minSec = max(minSec, tempMin);

			//두 가지 방향 중 최대가 빨리 떨어지는 시간
			int tempMax = max(inputX, l - inputX);
			maxSec = max(maxSec, tempMax);
		}

		cout << minSec << ' ' << maxSec << '\n';
	}

	return 0;
}