#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int money;
	cin >> money;
	int junMoney = money, sungMoney = money; //남은 현금
	int junCnt = 0, sungCnt = 0; //주식 수

	int duck[14];
	int cUp = 0, cDown = 0;
	for (int i = 0; i < 14; i++) {
		cin >> duck[i];

		//준형이가 매수할 수 있는 경우
		if (junMoney >= duck[i]) {
			junCnt += junMoney/duck[i];
			junMoney -= duck[i] * (junMoney / duck[i]);
		}

		//성민
		if (i == 0 || i==13)
			continue;
		if (duck[i - 1] < duck[i]) {
			cDown = 0;
			cUp++;
		}
		else if (duck[i - 1] > duck[i]) {
			cDown++;
			cUp = 0;
		}
		else {
			cDown = 0;
			cUp = 0;
		}

		//연속으로 감소하여 매수
		if (cDown >= 3) {
			if (sungMoney >= duck[i]) {
				sungCnt += sungMoney / duck[i];
				sungMoney -= duck[i] * (sungMoney / duck[i]);
			}
		}
		//연속으로 증가하여 매도
		else if (cUp >= 3) {
			sungMoney += duck[i] * sungCnt;
			sungCnt = 0;
		}
	}

	int junResult = junMoney + duck[13] * junCnt;
	int sungResult = sungMoney + duck[13]*sungCnt;

	if (junResult > sungResult)
		cout << "BNP";
	else if (junResult < sungResult)
		cout << "TIMING";
	else
		cout << "SAMESAME";

	return 0;
}