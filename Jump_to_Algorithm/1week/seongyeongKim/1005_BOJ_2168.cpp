/*
참고한 풀이 : https://sdev.tistory.com/1223
*/

#include <iostream>
using namespace std;

//최대 공약수, 재귀 호출을 이용
int gcd(int x, int y) {
    if (y == 0) {
        return x;
    }
    else {
        return gcd(y, x % y);
    }
}

int main()
{
    int x, y, result;

    cin >> x >> y;

    result = gcd(x, y);

    cout << x + y - result;

    return 0;
}