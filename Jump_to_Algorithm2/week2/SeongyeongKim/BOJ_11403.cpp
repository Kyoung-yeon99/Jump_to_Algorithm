#include <iostream>
#include <stdio.h>
#include <vector>
#include <cstring>

using namespace std;

vector<int> _graph[100];
int visited[100];

void dfs(int node) {
    for (int i = 0; i < _graph[node].size(); i++) {
        if (!visited[_graph[node][i]]) {
            visited[_graph[node][i]] = 1;
            dfs(_graph[node][i]);
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n;
    cin >> n;

    int inputNum;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> inputNum;
            //i노드와 연결된 노드들의 정보를 _graph[i]에 추가
            if (inputNum) _graph[i].push_back(j);
        }
    }

    for (int i = 0; i < n; i++) {
        memset(visited, 0, sizeof(visited));
        //i노드에서 갈수있는 노드를 dfs를 통해 탐색
        dfs(i);
        //방문할 수 있는 노드들은 visited에서 1로 갱신
        for (int j = 0; j < n; j++) {
            cout << visited[j] << ' ';
        }
        cout << "\n";
    }

    return 0;
}