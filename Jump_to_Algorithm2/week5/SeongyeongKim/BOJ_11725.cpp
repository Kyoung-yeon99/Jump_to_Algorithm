/*
예제 1) 트리 구조
     1
   6   4
 3    7  2
5
*/

#include <bits/stdc++.h>
using namespace std;

int N;
int arr[100001]; //인덱스의 부모노드
bool visited[100001];
vector<int> v[100001];

void dfs(int k) {
    visited[k] = true;
    for (int i = 0; i < v[k].size(); i++) {
        int next = v[k][i];
        if (!visited[next]) {
            arr[next] = k;
            dfs(next);
        }
    }
}

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        int x, y;
        cin >> x >> y;
        v[x].push_back(y);
        v[y].push_back(x);
    }

    dfs(1); //자식노드에 방문하여 부모 지정, 1부터 자식 노드 방문 시작

    for (int i = 2; i <= N; i++) cout << arr[i] << "\n";
}