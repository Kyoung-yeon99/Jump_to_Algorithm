#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n, m;
    int cardNum;
    vector<int> cards;
    int result = 0, combSum;

    cin >> n >> m;


    //while���� ���鼭 n�� ���� ���ϱ� ������ Ǯ�̰� ��� Ʋ����
    //while(n--){
    int temp = n;
    while (temp--) {
        cin >> cardNum;
        cards.push_back(cardNum);
    }

    //n���� ī�� �� 3���� ī���� ������ Ȯ���ϸ� �ǹǷ� 3�� for�� ���
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