#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, input;
    priority_queue<int, vector<int>, greater<>> pq;

    cin >> N;
    cin.ignore();
    for (int i=0; i<N; ++i) {
        cin >> input;
        if (input == 0) {
            if(!pq.empty()){
                int top = pq.top();
                cout << top << "\n";
                pq.pop();
            }
            else{
                cout << 0 << "\n";
            }
        }
        else {
            pq.push(input);
        }
    }
    return 0;
}