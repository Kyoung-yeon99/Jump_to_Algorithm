#include <bits/stdc++.h>
using namespace std;

int N, M, K;
int map[102][102];
bool visited[102][102];
int dy[] = { 0,0,-1,1 };
int dx[] = { 1,-1,0,0 };
queue<pair<int, int>> q;
vector<int> v; //음식물 크기 저장 벡터
int area = 1;  //음식물 크기

void BFS(int y, int x) {
    visited[y][x] = true;
    q.push(make_pair(y, x));

    while (!q.empty()) {
        y = q.front().first;
        x = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (ny<0 || nx<0 || ny>N || nx>M)
                continue;
            if (map[ny][nx] == 1 && visited[ny][nx] == 0) {
                visited[ny][nx] = true;
                q.push(make_pair(ny, nx));
                area++;
            }
        }
    }
}

//오름차순 sort에 사용하는 함수 - 두 정수 중 큰 것 선택
bool compare(int i, int j) {
    return i > j;
}

int main() {
    cin >> N >> M >> K;
    while (K--) {
        int r, c;
        cin >> r >> c;
        map[r][c] = 1;
    }

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            if (map[i][j] == 1 && visited[i][j] == 0) {
                BFS(i, j);
                v.push_back(area);
                area = 1;
            }
        }
    }

    sort(v.begin(), v.end(), compare); //오름차순 정렬
    cout << v[0]; //가장 큰 값 출력
}
