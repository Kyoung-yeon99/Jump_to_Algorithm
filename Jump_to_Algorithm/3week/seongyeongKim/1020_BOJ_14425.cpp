#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;


int main()
{
    int N, M;
    cin >> N >> M;

    vector<string> v;
    string s;
    for (int i = 0; i < N; i++) {
        cin >> s;
        v.push_back(s);
    }

    //binary_search�� �ϱ� ���� �������� ���� �ʿ�
    sort(v.begin(), v.end());

    int cnt = 0;
    for (int i = 0; i < M; i++) {
        cin >> s;

        //�׳� find�� ���ָ� ���ʰ� �߻��ϱ� ������
        //���� Ž���� ���� find ����
        if (binary_search(v.begin(), v.end(), s))
            cnt++;
    }

    cout << cnt;

    return 0;
}