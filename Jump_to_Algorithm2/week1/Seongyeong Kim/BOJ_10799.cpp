#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	stack<char> s;

	string str;
	cin >> str;

	int cnt = 0;
	for (int i = 0; i < str.size(); i++) {
		if (str[i] == '(')
			s.push('(');
		else {
			//�������̸�
			//������ ��ȣ ¦�� �ϳ� pop ���ְ�
			//�׵��� ���ÿ� ��� �ִ� ����� ������ �� �����
			if (str[i - 1] == '(') {
				s.pop();
				cnt += s.size();
			}
			//������� ���̸�
			//�ϳ� pop���ְ� ����� �� ���� �ϳ� �߰�
			else {
				s.pop();
				cnt++;
			}
		}
	}

	cout << cnt;

	return 0;
}