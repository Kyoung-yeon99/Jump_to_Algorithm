#include <iostream>
#include <string>
#include <set>
#include <sstream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);


    int N, M;
    string input;
    set<string> memo;

    cin >> N >> M;
    cin.ignore();

    for (int i=0; i<N; ++i) {
        getline(cin, input);
        memo.insert(input);
    }

    for (int i=0; i<M; ++i){
        getline(cin, input);
        stringstream ss(input);
        string keyword;

        while (getline(ss, keyword, ',')) {
          memo.erase(keyword);
        }
        cout << memo.size() << "\n";
    }

    return 0;
}
