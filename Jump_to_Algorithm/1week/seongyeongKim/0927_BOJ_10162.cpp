#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int time;
	cin >> time;

	int a=0, b=0, c = 0;

	a += time / 300;
	//a += (time >= 300) ? time / 300 : 0;
	time -= (a*300);

	b += time / 60;
	//b += (time >= 60) ? time / 60 : 0;
	time -= b * 60;

	c += time / 10;
	//c += (time >= 10) ? time / 10 : 0;
	time -= c * 10;

	if (time)
		cout << -1;
	else
		cout << a << ' ' << b << ' ' << c;

	return 0;
}