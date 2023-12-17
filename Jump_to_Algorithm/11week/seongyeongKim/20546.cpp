#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int money;
	cin >> money;
	int junMoney = money, sungMoney = money; //���� ����
	int junCnt = 0, sungCnt = 0; //�ֽ� ��

	int duck[14];
	int cUp = 0, cDown = 0;
	for (int i = 0; i < 14; i++) {
		cin >> duck[i];

		//�����̰� �ż��� �� �ִ� ���
		if (junMoney >= duck[i]) {
			junCnt += junMoney/duck[i];
			junMoney -= duck[i] * (junMoney / duck[i]);
		}

		//����
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

		//�������� �����Ͽ� �ż�
		if (cDown >= 3) {
			if (sungMoney >= duck[i]) {
				sungCnt += sungMoney / duck[i];
				sungMoney -= duck[i] * (sungMoney / duck[i]);
			}
		}
		//�������� �����Ͽ� �ŵ�
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