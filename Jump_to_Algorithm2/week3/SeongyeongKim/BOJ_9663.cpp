#include <bits/stdc++.h>
using namespace std;

int N;
int cnt = 0;

bool isused1[40]; // column�� �����ϰ� �ִ���
bool isused2[40]; // / ���� �밢���� �����ϰ� �ִ���
bool isused3[40]; // \ ���� �밢���� �����ϰ� �ִ���

//level��° �࿡ ���� ��ġ
void dfs(int level) {
    if (level == N) {
        cnt++;
        return;
    }

    for (int i = 0; i < N; i++) { // (level, i)�� ���� ���� ����
        // column�̳� �밢�� �߿� ���� �ִٸ� ���� Ž��
        if (isused1[i] || isused2[i + level] || isused3[level - i + N - 1])
            continue;
        //isused�� true�� �ٲ��ֹǷ� �̰��� �� ��ġ�� �Ұ����ϴٴ� ���� �ǹ�
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