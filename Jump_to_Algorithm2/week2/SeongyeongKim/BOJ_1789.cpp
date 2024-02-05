#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0); 

	long long S;
	cin >> S;

	long long N = 1, cnt = 0;

	//자연수 합이 S를 넘길 때까지 N를 계속 빼줌
	while (S >= 0) {
		S -= N;
		N++;
		cnt++;
	}

	//자연수 합이 S를 넘기므로 cnt 하나 빼줘야 함
	cout << --cnt;

	return 0;
}