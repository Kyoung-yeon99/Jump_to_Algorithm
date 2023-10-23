#include <iostream>
using namespace std;

/*  
	input되는 수의 개수 범위는 1~10,000,000으로 크지만
	input되는 수의 범위는 10,000보다 작으므로
	input되는 수를 입력 받는 족족 우선 순위 큐로 정렬하면 메모리 초과 발생
	따라서 입력 받는 수의 범위를 배열로 만들어서 개수를 증가하는 방식으로 풀이 진행
*/

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	long long num[10001] = { 0, };

	int N;
	cin >> N;

	int inputNum;
	for (int i = 0; i < N; i++) {
		//배열의 인덱스가 입력 받는 수가 되어 1씩 증가
		cin >> inputNum;
		num[inputNum]++;
	}

	//num을 처음부터 돌면서 0이 아닌 수면 그 수 만큼 인덱스를 반복해서 출력
	int cnt;
	for (int i = 1; i < 10001; i++) {
		cnt = num[i];

		while (cnt--)
			cout << i << '\n';
	}

	return 0;
}