#include <bits/stdc++.h>
using namespace std;

bool cmp(pair<int, int> a, pair<int, int> b) {
	//y��ǥ ��������
	if (a.second < b.second)
		return true;
	//y��ǥ ������ x��ǥ ��������
	else if (a.second == b.second)
		if (a.first < b.first)
			return true;
	return false;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	vector<pair<int, int>> v;
	int N;
	cin >> N;

	int x, y;
	for (int i = 0; i < N; i++) {
		cin >> x >> y;
		v.push_back({ x, y });
	}

	//����� ���� compare�� sort ����
	sort(v.begin(), v.end(), cmp);

	for (auto i : v)
		cout << i.first << ' ' << i.second << '\n';


	return 0;
}