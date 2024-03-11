#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    int arr[50];
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    sort(arr, arr + n);

    int ans = 4; // 최소 원소 개수를 나타내는 변수를 초기화

    for (int i = 0; i < n; i++) {
        // 현재 원소(arr[i])로부터 5 이상 차이나는 원소의 개수를 계산
        int tmp = distance(arr + i, lower_bound(arr, arr + n, arr[i] + 5));
        // 현재까지의 최소 원소 개수 갱신
        ans = min(ans, 5 - tmp);
    }

    cout << ans; // 최종 결과 출력

    return 0;
}
