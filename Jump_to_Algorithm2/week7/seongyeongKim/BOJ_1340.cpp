#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	string month, time, day;
	string eng_mon[12] = { "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" };
	int year, mon, dayarr[2] = {}, count = 0, hour, min, totalmin;
	cin >> month >> day >> year >> time;

	int m_arr[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

	//연도
	//윤년이면
	if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)) {		
		m_arr[1] = 29;
		totalmin = 366 * 24 * 60;
	}
	else
		totalmin = 365 * 24 * 60;

	int daysum = 0; //얼마나 지났는지

	//월
	for (int i = 0; i < 12; i++) {	
		if (month == eng_mon[i]) {
			//해당 월 전에 지나온 월들의 일 수 누적
			for (int j = 0; j < i; j++) {
				daysum += m_arr[j];
			}
			break;
		}
	}

	//일
	for (int i = 0; i < day.length() - 1; i++) {		
		dayarr[i] = day[i] - '0';
		count++;
	}

	//1이면 일이 한자리수
	if (count == 1)
		daysum += dayarr[0];
	//2면 두자리수
	else if (count == 2)
		daysum += dayarr[0] * 10 + dayarr[1];
	daysum--;

	//시간
	//시간 맨 앞자리가 0이면 시간이 한자리수만 유효
	if (time[0] == '0') {					
		hour = time[1] - '0';
	}
	//0이 아니면 두자리수가 유효
	else
		hour = (time[0] - '0') * 10 + (time[1] - '0');

	//분
	//분도 동일
	if (time[3] == '0') {					
		min = time[4] - '0';
	}
	else
		min = (time[3] - '0') * 10 + (time[4] - '0');

	int minsum = daysum * 24 * 60 + hour * 60 + min;

	double result = (double)minsum / totalmin * 100;
	printf("%0.9f\n", result);

	return 0;
}