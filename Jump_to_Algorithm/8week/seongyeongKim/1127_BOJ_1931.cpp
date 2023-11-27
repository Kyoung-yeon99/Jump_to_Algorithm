#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, start, end;
    int result = 1;
    vector<pair<int, int>> v; //�Է� ȸ������ �����ϴ� vector

    cin >> n;
    int temp = n;

    while (temp--) {
        cin >> start >> end;
        v.push_back({ end, start });
    }

    //������ �ð��� �������� ����
    sort(v.begin(), v.end());

    int endTime = v[0].first;
    for (int i = 1; i < n; i++) {
        //���� ������ ȸ�� ������ �ð�(endTime)�� 
        //���� Ž���ϴ� ȸ�� ���� �ð�(v[i])���� ���ų� ������, ���ǿ� �����ϴ� ������
        //result ������Ű��, endTime ��
        if (endTime <= v[i].second) {
            result++;
            endTime = v[i].first;
        }
    }

    cout << result;


    return 0;
}