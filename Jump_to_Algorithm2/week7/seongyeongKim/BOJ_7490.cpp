#include <bits/stdc++.h>
using namespace std;

void solve(int N, vector<string>& expression, int idx, int current, int sum) {
    // ���� ����: ������ �ϼ��� ���
    if (idx == N) {
        // ������� ������ ����� 0�� ��� ���
        if (sum + current == 0) {
            for (const string& s : expression) {
                cout << s;
            }
            cout << '\n';
        }
        return;
    }

    // ���� ���ڸ� �̾���� ���
    expression.push_back(to_string(N));
    solve(N, expression, idx + 1, current * 10 + N, sum);
    expression.pop_back();  // ��Ʈ��ŷ

    // '+'�� �߰��� ���
    expression.push_back("+");
    expression.push_back(to_string(N));
    solve(N, expression, idx + 1, N, sum + current);
    expression.pop_back();  // ��Ʈ��ŷ
    expression.pop_back();  // ��Ʈ��ŷ
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    for (int t = 0; t < T; ++t) {
        int N;
        cin >> N;

        vector<string> expression;
        solve(N, expression, 1, 1, 0);  // �ʱⰪ ����

        cout << '\n';  // �� �׽�Ʈ ���̽��� ��� ��� �� �� �� �߰�
    }

    return 0;
}
