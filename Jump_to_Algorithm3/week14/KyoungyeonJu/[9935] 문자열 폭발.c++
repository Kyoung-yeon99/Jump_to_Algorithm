#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    string s, bomb;
    cin >> s >> bomb;

    int s_len = s.length();
    int b_len = bomb.length();
    string t = "";

    for (int i=0; i<s_len; i++) {
      t += s[i];
      if (t.length() >= b_len) {
        bool flag = true;
        for (int j=0; j<b_len; j++) {
          if (bomb[j] != t[t.size()-b_len+j]) {
            flag = false;
            break;
          }
        }

        if (flag) {
            t.erase(t.size()-b_len,b_len);
        }
      }
    }

    if (t.empty())
      cout << "FRULA";
    else
      cout << t;

    return 0;
}
