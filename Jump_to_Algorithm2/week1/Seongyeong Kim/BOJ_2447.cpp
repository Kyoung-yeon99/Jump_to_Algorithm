/*
참고한 풀이 : https://winkite1226.tistory.com/119
*/

#include <bits/stdc++.h>
using namespace std;

void recur(int x, int y, int n) {
	//' '를 찍는 조건
	if ((x / n) % 3 == 1 && (y / n) % 3 == 1) {
		cout << ' ';
	}
	else {
		//위에 if 조건에 해당 안되면, 한 변의 길이 n이 3보다 작은 경우 '*' 찍기
		if (n / 3 == 0) {
			cout << '*';
		}
		else {
			recur(x, y, n / 3);
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int N;
	cin >> N;

	//각 좌표에 해당해서 이것는 '*'인지 ' '인지를 재귀로 검사하여 찍음
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			recur(i, j, N);
		}
		cout << '\n';
	}

	return 0;
}