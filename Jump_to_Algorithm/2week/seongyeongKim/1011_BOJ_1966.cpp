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

			q.push({ i, inputNum }); //인덱스와 우선순위 넣음
			pq.push(inputNum); //우선순위 큐를 활용해서 우선순위에 대한 판단
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