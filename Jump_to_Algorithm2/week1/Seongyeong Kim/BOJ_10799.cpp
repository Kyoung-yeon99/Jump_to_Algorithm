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
			//레이저이면
			//레이저 괄호 짝꿍 하나 pop 해주고
			//그동안 스택에 담겨 있는 막대기 개수들 다 담아줌
			if (str[i - 1] == '(') {
				s.pop();
				cnt += s.size();
			}
			//막대기의 끝이면
			//하나 pop해주고 막대기 끝 조각 하나 추가
			else {
				s.pop();
				cnt++;
			}
		}
	}

	cout << cnt;

	return 0;
}