#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0); 

	int A, B, N;
	cin >> A >> B >> N;
	
	int result = abs(A-B);
	int num;
	for (int i = 0; i < N; i++) {
		cin >> num;
		result = min(result, abs(num - B) + 1);
	}

	cout << result;

	return 0;
}