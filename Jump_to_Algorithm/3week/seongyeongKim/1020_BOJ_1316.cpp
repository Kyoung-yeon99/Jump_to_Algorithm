#include <iostream>
#include <string>
using namespace std;

bool groupWord(string s) {
    bool visited[26] = { false, };

    visited[s[0] - 'a'] = true;

    for (int i = 1; i < s.size(); i++) {
        int idx = s[i] - 'a';
        //앞에 알파벳과 다른 경우
        if (s[i - 1] != s[i]) {
            //이전에 나온 알파벳이면 그룹 단어가 아님
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
