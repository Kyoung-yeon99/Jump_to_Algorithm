#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int N, L;
	cin >> N >> L;

	//물 웅덩이 시작, 끝 담는 벡터
	vector<pair<int, int>> v;

	int start, end;
	for (int i = 0; i < N; i++) {
		cin >> start >> end;
		v.push_back({ start, end });
	}

	//웅덩이 시작점을 기준으로 벡터 정렬
	sort(v.begin(), v.end());

	int result = 0;
	int idx = 0;


	for (int i = 0; i < N; i++) {
		//현재 인덱스가 웅덩이 끝보다 크면 무시
		if (idx >= v[i].second)
			continue;

		//웅덩이의 끝이 idx를 넘어가면 -> 시작점을 idx로 갱신
		idx = max(idx, v[i].first);

		//널판지 개수 세기
		int cnt = (v[i].second - (idx + 1)) / L + 1;
		result += cnt;
		idx += L * cnt;
	}

	cout << result << '\n';

	return 0;
}