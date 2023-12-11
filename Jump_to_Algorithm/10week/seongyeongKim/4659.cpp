#include <bits/stdc++.h>
using namespace std;

// 모음이면 true, 자음이면 false 리턴
bool is_vowel(char c)
{
	if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
		return true;
	return false;
}

// 품질 평가
bool qe(string& s)
{
	bool flag = false;	// 적어도 하나의 모음이 포함되는지 - 조건 1
	int con = 0;		// 연속되는 자음의 개수
	int vow = 0;		// 연속되는 모음의 개수
	int i;

	for (i = 0; i < s.size(); i++)
	{
		if (is_vowel(s[i]))
		{
			flag = true;
			vow++;
			con = 0;
		}
		else
		{
			con++;
			vow = 0;
		}
		if (con == 3 || vow == 3) // 조건 2
		{
			return false;
		}
		if (i > 0 && s[i - 1] == s[i] && !(s[i] == 'e' || s[i] == 'o')) // 조건 3
		{
			return false;
		}
	}
	if (!flag) // 조건 1
	{
		return false;
	}
	return true;
}

int main()
{
	string s;

	while (1)
	{
		cin >> s;
		if (s.compare("end") == 0)
			break;
		if (qe(s))
			cout << "<" << s << "> is acceptable.\n";
		else
			cout << "<" << s << "> is not acceptable.\n";
	}
	return 0;
}