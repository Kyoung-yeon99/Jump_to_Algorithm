#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int N;
	cin >> N;

	int result = 0;

	while (N >= 0) {
		if (N % 5 == 0) {
			result += (N / 5);
			cout << result;
			return 0;
		}

		N -= 3;
		result++;
	}

	cout << -1;

	return 0;
}