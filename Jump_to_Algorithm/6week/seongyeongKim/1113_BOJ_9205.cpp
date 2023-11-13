#include <bits/stdc++.h>
using namespace std;

struct point {
	int x;
	int y;
};

point store[100];
point festival;
point home;
bool visited[100];
int storeNum;

bool check() {
	queue <pair<int, int>> q;
	q.push({ home.x, home.y });

	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		//현재 위치하고 있는 좌표(맥주가 20병이 다 있는 상태(집 or 편의점))에서
		//페스티벌까지의 거리가 1000이내 이면 true 반환 (happy 출력)
		if (abs(x - festival.x) + abs(y - festival.y) <= 1000) return true;

		//거리가 1000을 넘어가면 편의점을 탐색
		for (int i = 0; i < storeNum; i++) {
			//방문했다면 pass
			if (visited[i]) continue;
			//현재 위치한 곳과 편의점의 거리 계산
			int d = (abs(x - store[i].x) + abs(y - store[i].y));
			//거리가 1000이내이면 탐색할 수 있게 큐에 추가
			if (d <= 1000) {
				visited[i] = true;
				q.push({ store[i].x, store[i].y });
			}

		}
	}

	return false;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int testCaseNum;

	cin >> testCaseNum;

	while (testCaseNum--) {
		cin >> storeNum;
		cin >> home.x >> home.y;

		for (int i = 0; i < storeNum; i++) {
			cin >> store[i].x >> store[i].y;
		}
		cin >> festival.x >> festival.y;

		if (check()) cout << "happy\n";
		else cout << "sad\n";

		//visited 초기화
		memset(visited, 0, sizeof(visited));
	}

	return 0;
}