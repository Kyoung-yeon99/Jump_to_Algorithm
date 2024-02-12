#include <bits/stdc++.h>
using namespace std;

int N;
int cnt = 0;

bool isused1[40]; // column을 차지하고 있는지
bool isused2[40]; // / 방향 대각선을 차지하고 있는지
bool isused3[40]; // \ 방향 대각선을 차지하고 있는지

//level번째 행에 말을 배치
void dfs(int level) {
    if (level == N) {
        cnt++;
        return;
    }

    for (int i = 0; i < N; i++) { // (level, i)에 퀸을 놓을 예정
        // column이나 대각선 중에 말이 있다면 다음 탐색
        if (isused1[i] || isused2[i + level] || isused3[level - i + N - 1])
            continue;
        //isused를 true로 바꿔주므로 이곳은 말 배치가 불가능하다는 것을 의미
        isused1[i] = true;
        isused2[i + level] = true;
        isused3[level - i + N - 1] = true;
        dfs(level + 1);
        isused1[i] = false;
        isused2[i + level] = false;
        isused3[level - i + N - 1] = false;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N;
    dfs(0);
    cout << cnt;

    return 0;
}