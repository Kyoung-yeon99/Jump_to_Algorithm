/*
���� 1) Ʈ�� ����
     1
   6   4
 3    7  2
5
*/

#include <bits/stdc++.h>
using namespace std;

int N;
int arr[100001]; //�ε����� �θ���
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

    dfs(1); //�ڽĳ�忡 �湮�Ͽ� �θ� ����, 1���� �ڽ� ��� �湮 ����

    for (int i = 2; i <= N; i++) cout << arr[i] << "\n";
}