/*
* refer : https://velog.io/@danbibibi/%EB%B0%B1%EC%A4%80-14981%EB%B2%88-%ED%86%B1%EB%8B%88%EB%B0%94%ED%80%B4
*/
#include<iostream>
#include<cstring>
#include<string>
using namespace std;

string gear[4]; // N���� 0, S���� 1
int rotatenum[4]; //��ϵ��� ȸ�� ����

void rotation(int num, int dir) {

	memset(rotatenum, 0, sizeof(rotatenum));

	// 1. ��� �������� ȸ�� ���� ���ϱ� 
	rotatenum[num] = dir;
	for (int i = num + 1; i < 4; i++) {
		if (rotatenum[i - 1] != 0 && gear[i - 1][2] != gear[i][6]) {
			if (rotatenum[i - 1] == -1) rotatenum[i] = 1;
			else if (rotatenum[i - 1] == 1) rotatenum[i] = -1;
		}
	}
	for (int i = num - 1; i >= 0; i--) {
		if (rotatenum[i + 1] != 0 && gear[i + 1][6] != gear[i][2]) {
			if (rotatenum[i + 1] == -1) rotatenum[i] = 1;
			else if (rotatenum[i + 1] == 1) rotatenum[i] = -1;
		}
	}

	// 2. ��� ���� ȸ��
	for (int i = 0; i < 4; i++) {
		if (rotatenum[i] == -1) { // �ݽð���� ȸ��
			string s = gear[i].substr(1);
			s += gear[i][0];
			gear[i] = s;
		}
		else if (rotatenum[i] == 1) { // �ð���� ȸ��
			string s = gear[i].substr(0, gear[i].size() - 1);
			s = gear[i][gear[i].size() - 1] + s;
			gear[i] = s;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(0); 
	cin.tie(0); cout.tie(0);

	for (int i = 0; i < 4; i++) cin >> gear[i];
	int k, num, dir;  

	cin >> k;
	//k�� ȸ��
	while (k--) {
		cin >> num >> dir;
		rotation(num - 1, dir);
	}
	
	// �� K�� ȸ����Ų ���Ŀ� �� ��Ϲ����� ������ ���� ���
	int pow2[] = { 1, 2, 4, 8 };
	int ans = 0;
	for (int i = 0; i < 4; i++) ans += (gear[i][0] - '0') * pow2[i]; // char to int
	cout << ans;
}