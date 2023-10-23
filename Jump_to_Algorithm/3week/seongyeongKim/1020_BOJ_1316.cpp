#include <iostream>
#include <string>
using namespace std;

bool groupWord(string s) {
    bool visited[26] = { false, };

    visited[s[0] - 'a'] = true;

    for (int i = 1; i < s.size(); i++) {
        int idx = s[i] - 'a';
        //�տ� ���ĺ��� �ٸ� ���
        if (s[i - 1] != s[i]) {
            //������ ���� ���ĺ��̸� �׷� �ܾ �ƴ�
            if (visited[idx])
                return false;
        }
        visited[idx] = true;
    }
    return true;
}

int main()
{
    int N;
    cin >> N;

    int cnt = 0;
    string s;
    for (int i = 0; i < N; i++) {
        cin >> s;
        if (groupWord(s))
            cnt++;
    }

    cout << cnt;

    return 0;
}
