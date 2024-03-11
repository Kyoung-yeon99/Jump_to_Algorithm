/*
* 플로이드 워셜 : 모든 지점에서 다른 모든 지점까지의 최단 경로
* https://velog.io/@kimdukbae/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Floyd-Warshall-Algorithm
* 
* 참고한 풀이 : https://hackids.tistory.com/86
*/

#include <bits/stdc++.h>
using namespace std;

const int MAX = 101;

int n, m;
int net[MAX][MAX];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        int a, b; cin >> a >> b;
        net[a][b] = 1;
        net[b][a] = 1;
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i != j && net[i][j] != 1) {
                net[i][j] = 10000000;
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= n; k++) {
                if (net[j][i] + net[i][k] < net[j][k]) {
                    net[j][k] = net[j][i] + net[i][k];
                }

            }
        }
    }

    int val = 10000000;
    int res;
    for (int i = 1; i <= n; i++) {
        int tmp = 0;
        for (int j = 1; j <= n; j++) {
            tmp += net[i][j];
        }
        if (tmp < val) {
            val = tmp;
            res = i;
        }
    }

    cout << res;

    return 0;


	return 0;
}