#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int a1, a2, a3;

	cin >> a1 >> a2 >> a3;

	if (a1 + a2 + a3 == 180) {
		//if, else if ¼ø¼­°¡ ¹Ù²î¸é ¾ÈµÊ
		if (a1 == 60 && a2 == 60 && a3 == 60)
			cout << "Equilateral";
		else if (a1 == a2 || a1 == a3 || a2 == a3)
			cout << "Isosceles"; 
		else
			cout << "Scalene";
	}
	else
		cout << "Error";

	return 0;
}