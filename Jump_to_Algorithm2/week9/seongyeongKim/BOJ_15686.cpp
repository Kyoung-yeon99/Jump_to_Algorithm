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
    //idx�� chicken����Ʈ���� ��� ġŲ���� ���õǾ����� ǥ���ϴ� ��

    //��Ʈ��ŷ ���� �������� cnt�� ġŲ���� ������ ���������� ��
    //ġŲ �Ÿ� ���
    if (cnt == m) {
        int total_distance = 0;
        for (auto h : home) {
            int distance = 987654321;
            
            //������ ���� ���� ����� ġŲ ���� �������� ���ؾ� �ϹǷ�,
            //checked�� true�� ���� dfs�� �ȵ� 3���� ġŲ �� �� �ϳ���� �Ҹ�
            //���� 3���� ġŲ �� �߿��� ���� ���� ���̶� �Ÿ� ���� ª�� ������ distance�� �����Ͽ� total�� ����
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