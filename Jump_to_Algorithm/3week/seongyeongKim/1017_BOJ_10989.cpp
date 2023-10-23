#include <iostream>
using namespace std;

/*  
	input�Ǵ� ���� ���� ������ 1~10,000,000���� ũ����
	input�Ǵ� ���� ������ 10,000���� �����Ƿ�
	input�Ǵ� ���� �Է� �޴� ���� �켱 ���� ť�� �����ϸ� �޸� �ʰ� �߻�
	���� �Է� �޴� ���� ������ �迭�� ���� ������ �����ϴ� ������� Ǯ�� ����
*/

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	long long num[10001] = { 0, };

	int N;
	cin >> N;

	int inputNum;
	for (int i = 0; i < N; i++) {
		//�迭�� �ε����� �Է� �޴� ���� �Ǿ� 1�� ����
		cin >> inputNum;
		num[inputNum]++;
	}

	//num�� ó������ ���鼭 0�� �ƴ� ���� �� �� ��ŭ �ε����� �ݺ��ؼ� ���
	int cnt;
	for (int i = 1; i < 10001; i++) {
		cnt = num[i];

		while (cnt--)
			cout << i << '\n';
	}

	return 0;
}