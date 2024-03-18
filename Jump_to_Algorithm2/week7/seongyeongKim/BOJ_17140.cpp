/*
* ������ Ǯ�� : https://velog.io/@lamknh/C-%EB%B0%B1%EC%A4%80-17140-%EC%9D%B4%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4%EA%B3%BC-%EC%97%B0%EC%82%B0
*/

#include <bits/stdc++.h>
using namespace std;

int A[101][101] = { 0 }; // �迭
int idx[101] = { 0 }; // ���� ����

// ���Ľ� ���� ���� Ƚ�� Ŀ���� ������ ����
vector<pair<int, int> > v[101]; // ���� ���� ���� - cnt / num ������ ����
int r, c, k;

int row = 3, col = 3;

int sec = 0;

// v clear
void clear() {
    for (int i = 0; i < 101; i++) {
        v[i].clear();
    }
}

void mapClear() {
    for (int i = 0; i < col; i++) {
        for (int j = 0; j < row; j++) {
            A[i][j] = 0;
        }
    }
}

void R() {
    sec++;

    for (int i = 0; i < col; i++) {
        memset(idx, 0, sizeof(idx)); // ���� ���� �迭 �ʱ�ȭ

        for (int j = 0; j < row; j++) {
            idx[A[i][j]]++; // ���� ����
        }

        for (int j = 1; j < 101; j++) {
            // ���� �����ϸ�
            if (idx[j] > 0) {
                v[i].push_back({ idx[j], j });
            }
        }
    }

    mapClear();

    for (int i = 0; i < col; i++) {
        // ����ü�� sort �ȵ�. Pair ���
        sort(v[i].begin(), v[i].end()); // �������� - ���� ����Ƚ���� Ŀ���� ������, ���� Ŀ���� ������
    }

    // col�� ����
    for (int i = 0; i < col; i++) {
        int nrow = v[i].size() * 2;
        row = max(row, nrow);
        int index = 0;
        for (int j = 0; j < v[i].size(); j++) {
            A[i][index++] = v[i][j].second; // num
            A[i][index++] = v[i][j].first; // cnt
        }
    }
}

void C() {
    sec++;

    for (int i = 0; i < row; i++) {
        memset(idx, 0, sizeof(idx)); // ���� ���� �迭 �ʱ�ȭ
        for (int j = 0; j < col; j++) {
            idx[A[j][i]]++; // ���� ����
        }

        for (int j = 1; j < 101; j++) {
            // ���� �����ϸ�
            if (idx[j] > 0) {
                v[i].push_back({ idx[j], j });
            }
        }
    }

    mapClear();

    for (int i = 0; i < row; i++) {
        // ����ü�� sort �ȵ�. Pair ���
        sort(v[i].begin(), v[i].end()); // �������� - ���� ����Ƚ���� Ŀ���� ������, ���� Ŀ���� ������
    }

    // col�� ����
    for (int i = 0; i < row; i++) {
        int ncol = v[i].size() * 2;
        col = max(col, ncol);
        int index = 0;
        for (int j = 0; j < v[i].size(); j++) {
            A[index++][i] = v[i][j].second; // num
            A[index++][i] = v[i][j].first; // cnt
        }
    }
}

int main() {
    cin >> r >> c >> k;

    // 3 * 3
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> A[i][j];
        }
    }

    // R����, C���� ������� | 1�� �� �� ���� 1�� ����
    while (A[r - 1][c - 1] != k) {
        // ���� ���� �� ���� ������ ��쿡 ����
        if (col >= row) {
            R();
        }
        else {
            // ���� ���� < ���� ������ ��쿡 ����
            C();
        }

        clear(); // v clear

        if (sec > 100) {
            sec = -1;
            break;
        }
    }

    cout << sec;

    return 0;
}