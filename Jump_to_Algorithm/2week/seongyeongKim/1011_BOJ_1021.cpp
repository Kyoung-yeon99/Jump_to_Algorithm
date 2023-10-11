#include <iostream>
#include <deque>
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    int cnt = 0;

    deque<int> dq;
    for (int i = 1; i <= N; i++)
        dq.push_back(i);

    int x; //������ ��
    while (M--) {
        cin >> x;

        int idx; //������ ���� �ε���
        for (int i = 0; i < dq.size(); i++) {
            if (dq[i] == x) {
                idx = i;
                break;
            }
        }

        //������ ���� �տ��� 2��, �ڿ��� 3�� �����ϴ� ���� �ּ� ����� 
        if (idx <= dq.size() / 2) {
            while (true) {
                //������ �� ã���� Ż��
                if (dq.front() == x) {
                    dq.pop_front();
                    break;
                }

                cnt++;
                //������ ���� �ƴϸ� 2�� ���� ����
                dq.push_back(dq.front());
                dq.pop_front();
            }
        }
        else {
            while (true) {
                //������ �� ã���� Ż��
                if (dq.front() == x) {
                    dq.pop_front();
                    break;
                }

                cnt++;
                //������ ���� �ƴϸ� 3�� ���� ����
                dq.push_front(dq.back());
                dq.pop_back();
            }
        }
    }

    cout << cnt;

    return 0;
}