#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int N;
	cin >> N;

	vector<int> v;
	int tmp;
	while (N--) {
		cin >> tmp;
		v.push_back(tmp);
	}

	sort(v.begin(), v.end());

	int M;
	cin >> M;
	while (M--) {
		cin >> tmp;
		cout << upper_bound(v.begin(), v.end(), tmp) - lower_bound(v.begin(), v.end(), tmp) << ' ';
	}

	return 0;
}