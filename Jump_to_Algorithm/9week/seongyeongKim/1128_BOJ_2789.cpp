#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n, m;
    int cardNum;
    vector<int> cards;
    int result = 0, combSum;

    cin >> n >> m;


    //while문을 돌면서 n의 값이 변하기 때문에 풀이가 계속 틀렸음
    //while(n--){
    int temp = n;
    while (temp--) {
        cin >> cardNum;
        cards.push_back(cardNum);
    }

    //n장의 카드 중 3장의 카드의 조합을 확인하면 되므로 3중 for문 사용
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                combSum = cards[i] + cards[j] + cards[k];
                if (combSum <= m) {
                    result = max(result, combSum);
                }
            }
        }
    }

    cout << result;

    return 0;
}