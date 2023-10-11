#include <bits/stdc++.h>
using namespace std;

int main(void) {
	int t, n, m;
	cin >> t;

	while (t--) {
		cin >> n >> m;

		priority_queue<int> pq;
		queue<pair<int, int>> q;

		int cnt = 0;

		for (int i = 0; i < n; i++) {
			int inputNum;
			cin >> inputNum;

			q.push({ i, inputNum }); //�ε����� �켱���� ����
			pq.push(inputNum); //�켱���� ť�� Ȱ���ؼ� �켱������ ���� �Ǵ�
		}

		while (!q.empty()) {
			int idx = q.front().first;
			int prio = q.front().second;
			q.pop();

			if (pq.top() == prio) {
				pq.pop();
				cnt++;

				if (idx == m) {
					cout << cnt << "\n";
					break;
				}
			}
			else {
				q.push({ idx, prio });
			}
		}
	}



	return 0;
}