#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	string inputStr;

	cin >> inputStr;

	char criti = inputStr[0];
	int zeroGroup = 0;
	int oneGroup = 0;

	if (criti == '0')
		zeroGroup++;
	else
		oneGroup++;

	for (int i = 1; i < inputStr.length(); i++) {
		if (criti == inputStr[i])
			continue;
		else {
			if (inputStr[i] == '0')
				zeroGroup++;
			else
				oneGroup++;
			criti = inputStr[i];
		}
	}

	if ((zeroGroup + oneGroup) == 1)
		cout << 0;
	else {
		cout << min(zeroGroup, oneGroup);
	}

	return 0;
}