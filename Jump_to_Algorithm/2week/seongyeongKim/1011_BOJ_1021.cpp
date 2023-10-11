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

    int x; //빼야할 수
    while (M--) {
        cin >> x;

        int idx; //삭제할 수의 인덱스
        for (int i = 0; i < dq.size(); i++) {
            if (dq[i] == x) {
                idx = i;
                break;
            }
        }

        //반으로 갈라서 앞에는 2번, 뒤에는 3번 연산하는 것이 최소 연산수 
        if (idx <= dq.size() / 2) {
            while (true) {
                //빼야할 수 찾으면 탈출
                if (dq.front() == x) {
                    dq.pop_front();
                    break;
                }

                cnt++;
                //빼야할 수가 아니면 2번 연산 수행
                dq.push_back(dq.front());
                dq.pop_front();
            }
        }
        else {
            while (true) {
                //빼야할 수 찾으면 탈출
                if (dq.front() == x) {
                    dq.pop_front();
                    break;
                }

                cnt++;
                //빼야할 수가 아니면 3번 연산 수행
                dq.push_front(dq.back());
                dq.pop_back();
            }
        }
    }

    cout << cnt;

    return 0;
}