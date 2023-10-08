#include <iostream>
using namespace std;

int N; //�ҽ��� ��
int M; //��а� ��

int GCD(int x, int y) {
	if (x % y == 0)
		return y;
	return (GCD(y, x % y));
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> M;

	//��а����� �ִ� ����� ���� ����
	cout << M - GCD(N, M);

	return 0;
}