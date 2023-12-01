#include <bits/stdc++.h>
using namespace std;

int main(void) {
	int n, m;
	cin >> n >> m;
	vector<int> v;


	for (int i = 0; i < n; i++) {
		int treeLen;
		cin >> treeLen;

		v.push_back(treeLen);
	}

	int maxLen = *max_element(v.begin(), v.end());
	int minLen = 0;
	int result = 0;

	//�̺� Ž���ε�, mid ���� ���Ͽ� ������ �����ϴ� ���� �ƴ�
	//������ �� �ִ� ������ ���̸� ������ ������ ����
	while (minLen <= maxLen) {
		long long int totalLen = 0;
		int mid = (minLen + maxLen) / 2;

		for (int i : v) {
			//������ �� �ִ� ���� ���� ���
			if (i > mid) totalLen += (i - mid);
		}

		if (totalLen < m) {
			maxLen = mid - 1;
		}
		else {
			result = mid;
			minLen = mid + 1;
		}
	}

	cout << result;

	return 0;
}