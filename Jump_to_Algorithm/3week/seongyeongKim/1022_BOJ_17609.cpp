#include <bits/stdc++.h>
using namespace std;

string s;

//투포인터를 사용하여 회문인지 유사회문인지 판단
int palin(int left, int right, int first) {
	//left가 right보다 작을 때까지 진행
	while (left < right) {
		//다른게 처음 -> 유사회문인지 판단
		//다른게 처음이 아니면 -> 2 출력
		if (s[left] != s[right]) {
			if (first) {
				//지워야 하는 문자가 앞인지, 뒤인지 둘다 확인해 봐야 함
				//지우고서 결과가 0이면 유사 회문
				if (palin(left + 1, right, false) == 0 || palin(left, right - 1, false) == 0)
					return 1;
			}
			return 2;
		}
		left++;
		right--;
	}
	return 0;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int T;
	cin >> T;


	while (T--) {
		cin >> s;
		cout << palin(0, s.length() - 1, true) << '\n';
	}

	return 0;
}
