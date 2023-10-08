#include <iostream>
using namespace std;

int N; //소시지 수
int M; //평론가 수

int GCD(int x, int y) {
	if (x % y == 0)
		return y;
	return (GCD(y, x % y));
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> M;

	//평론가에서 최대 공약수 빼면 정답
	cout << M - GCD(N, M);

	return 0;
}