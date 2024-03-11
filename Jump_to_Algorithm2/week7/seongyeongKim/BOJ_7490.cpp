#include <bits/stdc++.h>
using namespace std;

void solve(int N, vector<string>& expression, int idx, int current, int sum) {
    // 기저 조건: 수식이 완성된 경우
    if (idx == N) {
        // 만들어진 수식의 결과가 0인 경우 출력
        if (sum + current == 0) {
            for (const string& s : expression) {
                cout << s;
            }
            cout << '\n';
        }
        return;
    }

    // 현재 숫자를 이어붙인 경우
    expression.push_back(to_string(N));
    solve(N, expression, idx + 1, current * 10 + N, sum);
    expression.pop_back();  // 백트래킹

    // '+'를 추가한 경우
    expression.push_back("+");
    expression.push_back(to_string(N));
    solve(N, expression, idx + 1, N, sum + current);
    expression.pop_back();  // 백트래킹
    expression.pop_back();  // 백트래킹
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
        solve(N, expression, 1, 1, 0);  // 초기값 설정

        cout << '\n';  // 각 테스트 케이스의 결과 출력 후 빈 줄 추가
    }

    return 0;
}
