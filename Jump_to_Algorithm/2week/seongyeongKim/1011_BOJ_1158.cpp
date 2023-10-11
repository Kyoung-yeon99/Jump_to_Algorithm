#include <iostream>
#include <queue>
using namespace std;

int main()
{
    int N, K;
    cin >> N >> K;

    queue<int> q;
    for (int i = 0; i < N; i++) {
        q.push(i + 1);
    }

    cout << "<";

    while (q.size() > 1) {
        for (int i = 0; i < K - 1; i++) {
            //k번째 수가 아니면 큐 맨 앞 원소를 뒤로
            q.push(q.front());
            q.pop();
        }
        //k번째면 출력
        cout << q.front() << ", ";
        q.pop();
    }

    cout << q.front() << ">";

    return 0;
}
