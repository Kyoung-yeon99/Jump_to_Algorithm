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

    int ans = 4; // �ּ� ���� ������ ��Ÿ���� ������ �ʱ�ȭ

    for (int i = 0; i < n; i++) {
        // ���� ����(arr[i])�κ��� 5 �̻� ���̳��� ������ ������ ���
        int tmp = distance(arr + i, lower_bound(arr, arr + n, arr[i] + 5));
        // ��������� �ּ� ���� ���� ����
        ans = min(ans, 5 - tmp);
    }

    cout << ans; // ���� ��� ���

    return 0;
}
