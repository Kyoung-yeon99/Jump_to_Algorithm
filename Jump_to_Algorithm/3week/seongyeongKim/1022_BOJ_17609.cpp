#include <bits/stdc++.h>
using namespace std;

string s;

//�������͸� ����Ͽ� ȸ������ ����ȸ������ �Ǵ�
int palin(int left, int right, int first) {
	//left�� right���� ���� ������ ����
	while (left < right) {
		//�ٸ��� ó�� -> ����ȸ������ �Ǵ�
		//�ٸ��� ó���� �ƴϸ� -> 2 ���
		if (s[left] != s[right]) {
			if (first) {
				//������ �ϴ� ���ڰ� ������, ������ �Ѵ� Ȯ���� ���� ��
				//����� ����� 0�̸� ���� ȸ��
				if (palin(left + 1, right, false) == 0 || palin(left, right - 1, false) == 0)
					return 1;
			}
			return 2;
		}
		left++;
		right--;
	}
	return 0;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int T;
	cin >> T;


	while (T--) {
		cin >> s;
		cout << palin(0, s.length() - 1, true) << '\n';
	}

	return 0;
}
