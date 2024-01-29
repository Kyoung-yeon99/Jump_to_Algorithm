#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int N;
	cin >> N;

	string str;
	stack<char> s;
	bool rightStr;


	while (N--) {
		rightStr = true;
		cin >> str;

		for (auto c : str) {
			if (c == '(') {
				s.push('(');
			}
			else {
				if (!s.empty())
					s.pop();
				else 
					rightStr = false;
			}
		}
		
		if (!s.empty())
			rightStr = false;

		if (rightStr)
			cout << "YES\n";
		else {
			cout << "NO\n";
			//스택 초기화
			while (!s.empty())
				s.pop();
		}
	}

	return 0;
}