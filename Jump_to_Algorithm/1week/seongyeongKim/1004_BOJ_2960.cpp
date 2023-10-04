#include <iostream>
using namespace std;

bool visited[1001];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int N, K;
	cin >> N >> K;

	int cnt = 0;

	int ctri = 2;
	while (true) {
		for (int i = ctri; i <= N; i += ctri) {
			if (!visited[i]) {
				cnt++;
				//cout << i << " ";
				visited[i] = true;
				if (cnt == K) {
					cout << i;
					return 0;
				}
			}
		}

		for (int i = 2; i < 1001; i++) {
			if (!visited[i]) {
				ctri = i;
				break;
			}
		}
	}

	return 0;
}