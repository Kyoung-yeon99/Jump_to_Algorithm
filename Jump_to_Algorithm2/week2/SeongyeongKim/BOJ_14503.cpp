#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

//0 : 북, 1 : 동, 2 : 남, 3 : 서
int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0, -1 };
int n, m;

int _map[50][50];
int rX, rY, rDir; // ((x,y), direction)
int cnt = 0;

void step1() {
	if (_map[rX][rY] == 0) {
		_map[rX][rY] = 2;
		cnt++;
	}
}


void play() {
	while (true) {
		step1();

		bool step2go = true;

		//step3
		for (int i = 0; i < 4; i++) {
			int nDir = (rDir - i + 3) % 4; //반시계방향 회전
			int nx = rX + dx[nDir];
			int ny = rY + dy[nDir];

			if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

			if (_map[nx][ny] == 0) {
				rX = nx;
				rY = ny;
				rDir = nDir;
				step2go = false;
				break; //break를 안하면 i가 4가 될때까지 실행하므로 원하는 값 안나옴
			}
		}

		//step2
		if (step2go) {
			int nx = rX + dx[(rDir + 2) % 4];
			int ny = rY + dy[(rDir + 2) % 4];

			if (nx < 0 || nx >= n || ny < 0 || ny >= m) return;

			if (_map[nx][ny] != 1) {
				rX = nx;
				rY = ny;
			}
			else {
				return;
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m;

	int x, y, dir;
	cin >> rX >> rY >> rDir;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> _map[i][j];
		}
	}

	play();
	cout << cnt;

	return 0;
}