#include <bits/stdc++.h>
using namespace std;

int N, K;
int tall[300000];
int diff[300000];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);  cout.tie(0); 

	cin >> N >> K;

	for (int i = 0; i < N; i++) {
		cin >> tall[i];
	}

	for (int i = 0; i < N - 1; i++) {
		diff[i] = tall[i + 1] - tall[i];
	}

	sort(diff, diff + N - 1);

	long long answer = 0;
	for (int i = 0; i < N - K; i++) {
		answer += diff[i];
	}

	cout << answer;

	return 0;
}