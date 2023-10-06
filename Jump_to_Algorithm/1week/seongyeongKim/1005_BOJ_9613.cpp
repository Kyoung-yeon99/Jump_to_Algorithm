#include <iostream>
#include <algorithm>
using namespace std;

int t, n, inputNum;
long long sum = 0;
int num[100];
int twoNum[2];
bool visited[100];

int gcd(int num1, int num2) {
    int minNum = min(num1, num2);

    for (int i = minNum; i >= 1; i--) {
        if (num1 % i == 0 && num2 % i == 0) {
            return i;
        }
    }

    return 1;
}

void dfs(int idx, int level) {
    if (level == 2) {
        sum += gcd(twoNum[0], twoNum[1]);
        //cout<< twoNum[0] <<", "<< twoNum[1]<<'\n';
        return;
    }

    for (int i = idx; i < n; i++) {
        if (!visited[i]) {
            visited[i] = true;
            twoNum[level] = num[i];
            dfs(i + 1, level + 1);
            visited[i] = false;
        }
    }
}

int main()
{
    cin >> t;

    while (t--) {
        sum = 0;
        cin >> n;

        for (int i = 0; i < n; i++) {
            cin >> num[i];
        }

        dfs(0, 0);
        cout << sum << '\n';

        for (int i = 0; i < n; i++) {
            visited[i] = false;
        }
    }

    return 0;
}