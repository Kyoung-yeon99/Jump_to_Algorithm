#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	long long N, M;
	long long input;

	vector<long long> v;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> input;
		v.push_back(input);
	}
	sort(v.begin(), v.end());
	
	cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> input;
		cout << binary_search(v.begin(), v.end(), input) << ' ';
	}

	return 0;
}