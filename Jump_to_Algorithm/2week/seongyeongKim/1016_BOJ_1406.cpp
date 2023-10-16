#include <iostream>
#include <string>
#include <list>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	string s;
	cin >> s;
	
	int num;
	cin >> num;

	char order;

	list<char> l(s.begin(), s.end());
	auto curs = l.end();

	while (num--) {
		cin >> order;

		if (order == 'L') {
			if (curs != l.begin())
				curs--;
		}
		else if (order == 'D') {
			if (curs != l.end())
				curs++;
		}
		else if (order == 'B') {
			if (curs != l.begin())
				//지워진 다음 요소의 위치를 전달
				curs = l.erase(--curs);
		}
		else if (order == 'P') {
			char input;
			cin >> input;

			l.insert(curs, input);
		}
	}

	for (auto it = l.begin(); it != l.end(); it++) {
		cout << *it;
	}


	return 0;
}