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

    //binary_search를 하기 위한 조건으로 정렬 필요
    sort(v.begin(), v.end());

    int cnt = 0;
    for (int i = 0; i < M; i++) {
        cin >> s;

        //그냥 find를 해주면 시초가 발생하기 때문에
        //이진 탐색을 통해 find 진행
        if (binary_search(v.begin(), v.end(), s))
            cnt++;
    }

    cout << cnt;

    return 0;
}