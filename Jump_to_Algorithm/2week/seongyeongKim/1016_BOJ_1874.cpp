#include <bits/stdc++.h>
using namespace std;

int main(void) {
	int n, inputNum;
	int i = 1; //스택에 들어갈 수 시작
	stack<int> s;
	string result = "";

	cin >> n;

	while (n--) {
		cin >> inputNum;

		if (i <= inputNum) {
			while (i <= inputNum) {
				s.push(i);
				result += '+';
				i++;
			}

			s.pop();
			result += '-';
		}
		else {
			if (s.top() < inputNum) {
				cout << "NO";
				return 0;
			}
			else {
				s.pop();
				result += '-';
			}
		}
	}

	for (auto str : result) {
		cout << str << "\n";
	}

	return 0;
}