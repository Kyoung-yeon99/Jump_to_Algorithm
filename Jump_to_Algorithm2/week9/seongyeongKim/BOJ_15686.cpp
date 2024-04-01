#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int res = 987654321;
vector<pair<int, int>> home;
vector<pair<int, int>> chicken;
vector<bool> checked;

int n, m;

void dfs(int idx, int cnt) {
    //idx는 chicken리스트에서 어느 치킨집이 선택되었는지 표시하는 것

    //백트래킹 종료 조건으로 cnt가 치킨집의 개수와 동일해졌을 때
    //치킨 거리 계산
    if (cnt == m) {
        int total_distance = 0;
        for (auto h : home) {
            int distance = 987654321;
            
            //집으로 부터 가장 가까운 치킨 집이 무엇인지 구해야 하므로,
            //checked가 true면 현재 dfs에 픽된 3개의 치킨 집 중 하나라는 소리
            //따라서 3개의 치킨 집 중에서 가장 현재 집이랑 거리 가장 짧은 것으로 distance를 갱신하여 total에 더함
            for (int i = 0; i < chicken.size(); ++i) {
                if (checked[i]) {
                    int r2 = chicken[i].first;
                    int c2 = chicken[i].second;
                    distance = min(distance, abs(h.first - r2) + abs(h.second - c2));
                }
            }
            total_distance += distance;
        }
        res = min(res, total_distance);
        return;
    }
    if (idx >= chicken.size()) {
        return;
    }

    checked[idx] = true;
    dfs(idx + 1, cnt + 1);
    checked[idx] = false;
    dfs(idx + 1, cnt);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n >> m;

    home.clear();
    chicken.clear();
    checked.clear();

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            int cell;
            cin >> cell;
            if (cell == 1) {
                home.push_back({ i, j });
            }
            else if (cell == 2) {
                chicken.push_back({ i, j });
            }
        }
    }

    checked.resize(chicken.size(), false);

    dfs(0, 0);

    cout << res << endl;

    return 0;
}