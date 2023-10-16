#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int N, L;
	cin >> N >> L;

	//�� ������ ����, �� ��� ����
	vector<pair<int, int>> v;

	int start, end;
	for (int i = 0; i < N; i++) {
		cin >> start >> end;
		v.push_back({ start, end });
	}

	//������ �������� �������� ���� ����
	sort(v.begin(), v.end());

	int result = 0;
	int idx = 0;


	for (int i = 0; i < N; i++) {
		//���� �ε����� ������ ������ ũ�� ����
		if (idx >= v[i].second)
			continue;

		//�������� ���� idx�� �Ѿ�� -> �������� idx�� ����
		idx = max(idx, v[i].first);

		//������ ���� ����
		int cnt = (v[i].second - (idx + 1)) / L + 1;
		result += cnt;
		idx += L * cnt;
	}

	cout << result << '\n';

	return 0;
}