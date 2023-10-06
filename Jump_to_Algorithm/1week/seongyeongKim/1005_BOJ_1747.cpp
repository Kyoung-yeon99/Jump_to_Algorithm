#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
using namespace std;

int N;

//�Ҽ����� �Ǻ�
bool decimal(int num) {
    if (num < 2)
        return false;

    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0)
            return false;
    }
    return true;
}

//�Ӹ�������� �Ⱥ�
bool palin(int num) {
    string front, back;

    string str = to_string(num);
    front = str;
    reverse(str.begin(), str.end());
    back = str;

    if (front == back)
        return true;
    else
        return false;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N;

    //N = (N>100) ? N : 101;

    while (true) {
        if (decimal(N) && palin(N)) {
            cout << N;
            break;
        }
        N++;
    }

    return 0;
}
