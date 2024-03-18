/*
* 참고한 풀이 : https://velog.io/@lamknh/C-%EB%B0%B1%EC%A4%80-17140-%EC%9D%B4%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4%EA%B3%BC-%EC%97%B0%EC%82%B0
*/

#include <bits/stdc++.h>
using namespace std;

int A[101][101] = { 0 }; // 배열
int idx[101] = { 0 }; // 개수 세기

// 정렬시 숫자 등장 횟수 커지는 순서가 먼저
vector<pair<int, int> > v[101]; // 개수 저장 벡터 - cnt / num 순서로 저장
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
        memset(idx, 0, sizeof(idx)); // 개수 세는 배열 초기화

        for (int j = 0; j < row; j++) {
            idx[A[i][j]]++; // 개수 세기
        }

        for (int j = 1; j < 101; j++) {
            // 숫자 존재하면
            if (idx[j] > 0) {
                v[i].push_back({ idx[j], j });
            }
        }
    }

    mapClear();

    for (int i = 0; i < col; i++) {
        // 구조체는 sort 안됨. Pair 써야
        sort(v[i].begin(), v[i].end()); // 오름차순 - 수의 등장횟수가 커지는 순으로, 수가 커지는 순으로
    }

    // col은 고정
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
        memset(idx, 0, sizeof(idx)); // 개수 세는 배열 초기화
        for (int j = 0; j < col; j++) {
            idx[A[j][i]]++; // 개수 세기
        }

        for (int j = 1; j < 101; j++) {
            // 숫자 존재하면
            if (idx[j] > 0) {
                v[i].push_back({ idx[j], j });
            }
        }
    }

    mapClear();

    for (int i = 0; i < row; i++) {
        // 구조체는 sort 안됨. Pair 써야
        sort(v[i].begin(), v[i].end()); // 오름차순 - 수의 등장횟수가 커지는 순으로, 수가 커지는 순으로
    }

    // col은 고정
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

    // R연산, C연산 순서대로 | 1번 할 때 마다 1초 지남
    while (A[r - 1][c - 1] != k) {
        // 행의 개수 ≥ 열의 개수인 경우에 적용
        if (col >= row) {
            R();
        }
        else {
            // 행의 개수 < 열의 개수인 경우에 적용
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