/*
참고한 풀이 : https://kimjingo.tistory.com/114
*/
#include <bits/stdc++.h>
using namespace std;

int T;
int N;
vector<int> v_pre;
vector<int> v_in;


void post_order(int start, int end, int pos) {
    for (int i = start; i < end; ++i) {
        if (v_in[i] == v_pre[pos]) {
            post_order(start, i, pos + 1);
            post_order(i + 1, end, pos + 1 + i - start);
            cout << v_pre[pos] << ' ';
        }
    }
}

void solve() {
    int root_idx = 0;
    post_order(root_idx, N, 0);
    cout << endl;
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> T;

    for (int i = 0; i < T; ++i) {
        cin >> N;
        v_pre = vector<int>(N);
        v_in = vector<int>(N);

        for (int j = 0; j < N; ++j) {
            cin >> v_pre[j];
        }
        for (int j = 0; j < N; ++j) {
            cin >> v_in[j];
        }
        solve();
    }
}
