#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n, inputNum;
	string op;
	queue<int> q;

	cin >> n;

	while (n--) {
		cin >> op;

		if (op == "push") {
			cin >> inputNum;
			q.push(inputNum);
		}
		else if (op == "pop") {
			if (!q.empty()) {
				cout << q.front() << '\n';
				q.pop();
			}
			else cout << "-1\n";
		}
		else if (op == "size") {
			cout << q.size() << '\n';
		}
		else if (op == "empty") {
			if (!q.empty()) cout << "0\n";
			else cout << "1\n";
		}
		else if (op == "front") {
			if (!q.empty()) {
				cout << q.front() << '\n';
			}
			else cout << "-1\n";
		}
		else if (op == "back") {
			if (!q.empty()) {
				cout << q.back() << '\n';
			}
			else cout << "-1\n";
		}
	}

	return 0;
}