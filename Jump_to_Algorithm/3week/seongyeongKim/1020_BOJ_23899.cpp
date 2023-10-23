#include <iostream>

using namespace std;


int N;
int before[10000], after[10000];

bool isEqual() {
    for (int i = 0; i < N; i++) {
        if (before[i] != after[i])
            return false;
    }
    return true;
}

int main()
{
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> before[i];
    }

    for (int i = 0; i < N; i++) {
        cin >> after[i];
    }

    //ó�� �迭�� �������� Ȯ��
    if (isEqual()) {
        cout << 1;
        return 0;
    }

    //���� ���� ����
    for (int i = 0; i < N - 1; i++) {
        int maxValue = -1, maxIdx = -1;
        for (int j = 0; j < N - i; j++) {
            if (maxValue < before[j]) {
                maxValue = before[j];
                maxIdx = j;
            }
        }
        before[maxIdx] = before[N - i - 1];
        before[N - i - 1] = maxValue;

        //���� 1step ������ �� after�� ��ġ�ϴ��� Ȯ��
        if (isEqual()) {
            cout << 1;
            return 0;
        }
    }

    cout << 0;

    return 0;
}