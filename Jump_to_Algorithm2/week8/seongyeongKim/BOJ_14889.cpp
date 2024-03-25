#include <bits/stdc++.h>
using namespace std;

int n;
int graph[21][21];
bool checked[21]; //true면 스타트팀, false면 링크팀
int result = 987654321;

void dfs(int level, int idx) {
    //dfs 탈출 조건
    //팀 계산
    if (level == n / 2) {
        int s_score = 0;
        int l_score = 0;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                //스타트팀
                if (checked[i] && checked[j]) {
                    s_score += graph[i][j];
                }
                //링크팀
                else if (!checked[i] && !checked[j]) {
                    l_score += graph[i][j];
                }
            }
        }
        //스타트와 링크 점수 차 최솟값 갱신
        result = min(result, abs(s_score - l_score));
        return;
    }

    if (idx >= n) {
        return;
    }

    checked[idx] = true;
    dfs(level + 1, idx + 1);
    checked[idx] = false;
    dfs(level, idx + 1);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> graph[i][j];
        }
    }

    dfs(0, 0);
    cout << result << endl;

    return 0;
}