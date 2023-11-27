#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, start, end;
    int result = 1;
    vector<pair<int, int>> v; //입력 회의정보 저장하는 vector

    cin >> n;
    int temp = n;

    while (temp--) {
        cin >> start >> end;
        v.push_back({ end, start });
    }

    //끝나는 시간을 기준으로 정렬
    sort(v.begin(), v.end());

    int endTime = v[0].first;
    for (int i = 1; i < n; i++) {
        //현재 기준인 회의 끝나는 시간(endTime)이 
        //지금 탐색하는 회의 시작 시간(v[i])보다 같거나 작으면, 조건에 부합하는 것으로
        //result 증가시키고, endTime 갱
        if (endTime <= v[i].second) {
            result++;
            endTime = v[i].first;
        }
    }

    cout << result;


    return 0;
}