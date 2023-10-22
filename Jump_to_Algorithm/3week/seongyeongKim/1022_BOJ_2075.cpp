#include <bits/stdc++.h>
using namespace std;

int _map[2250000];

int main() {
	ios::sync_with_stdio(0); 
	cin.tie(0); cout.tie(0);

	int N;

	cin >> N; 
	for (int i = 0; i < N*N; i++) {
		cin >> _map[i];
	}

	sort(_map, _map + (N * N));
	cout << _map[N * N - N];

	return 0;
}