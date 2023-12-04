#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int N, M;
	cin >> M >> N;

	vector<int> v;
	int len;
	for (int i = 0; i < M; i++) {
		cin >> len;
		v.push_back(len);
	}

	//이분 탐색
	int left = 1; //가장 작은 길이
	int right = *max_element(v.begin(), v.end()); //과자에서 가장 긴 길이
	
	int ans = 0;
	sort(v.rbegin(), v.rend());
	while (left <= right) {
		int cnt = 0;
		int mid = (left + right) / 2;
		for (int i = 0; i < M; i++) {
			cnt += v[i] / mid;
		}
		if (cnt < N) {
			right = mid - 1;
		}
		else {
			ans = mid;
			left = mid + 1;
		}
	}
	cout << ans;

	return 0;
}