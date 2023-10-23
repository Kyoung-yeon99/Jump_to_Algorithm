#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    vector<int> v, input;

    int N;
    cin >> N;

    int num;
    for (int i = 0; i < N; i++) {
        cin >> num;
        v.push_back(num);
        input.push_back(num);
    }

    //벡터 정렬
    sort(v.begin(), v.end());
    //중복 제거
    v.erase(unique(v.begin(), v.end()), v.end());

    for (int i = 0; i < N; i++) {
        //lower_bound는 input[i]가 처음 등장하는 위치 전달
        cout << lower_bound(v.begin(), v.end(), input[i]) - v.begin() << ' ';
    }

    return 0;
}