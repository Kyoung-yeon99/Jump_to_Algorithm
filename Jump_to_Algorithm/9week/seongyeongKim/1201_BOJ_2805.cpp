#include <bits/stdc++.h>
using namespace std;

int main(void) {
	int n, m;
	cin >> n >> m;
	vector<int> v;


	for (int i = 0; i < n; i++) {
		int treeLen;
		cin >> treeLen;

		v.push_back(treeLen);
	}

	int maxLen = *max_element(v.begin(), v.end());
	int minLen = 0;
	int result = 0;

	//이분 탐색인데, mid 값을 비교하여 범위를 수정하는 것이 아닌
	//가져갈 수 있는 나무의 길이를 생각해 범위를 수정
	while (minLen <= maxLen) {
		long long int totalLen = 0;
		int mid = (minLen + maxLen) / 2;

		for (int i : v) {
			//가져갈 수 있는 나무 길이 계산
			if (i > mid) totalLen += (i - mid);
		}

		if (totalLen < m) {
			maxLen = mid - 1;
		}
		else {
			result = mid;
			minLen = mid + 1;
		}
	}

	cout << result;

	return 0;
}