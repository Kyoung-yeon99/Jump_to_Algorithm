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

		//���� ��ġ�ϰ� �ִ� ��ǥ(���ְ� 20���� �� �ִ� ����(�� or ������))����
		//�佺Ƽ�������� �Ÿ��� 1000�̳� �̸� true ��ȯ (happy ���)
		if (abs(x - festival.x) + abs(y - festival.y) <= 1000) return true;

		//�Ÿ��� 1000�� �Ѿ�� �������� Ž��
		for (int i = 0; i < storeNum; i++) {
			//�湮�ߴٸ� pass
			if (visited[i]) continue;
			//���� ��ġ�� ���� �������� �Ÿ� ���
			int d = (abs(x - store[i].x) + abs(y - store[i].y));
			//�Ÿ��� 1000�̳��̸� Ž���� �� �ְ� ť�� �߰�
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

		//visited �ʱ�ȭ
		memset(visited, 0, sizeof(visited));
	}

	return 0;
}