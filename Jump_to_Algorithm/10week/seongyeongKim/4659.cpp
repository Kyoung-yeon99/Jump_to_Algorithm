#include <bits/stdc++.h>
using namespace std;

// �����̸� true, �����̸� false ����
bool is_vowel(char c)
{
	if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
		return true;
	return false;
}

// ǰ�� ��
bool qe(string& s)
{
	bool flag = false;	// ��� �ϳ��� ������ ���ԵǴ��� - ���� 1
	int con = 0;		// ���ӵǴ� ������ ����
	int vow = 0;		// ���ӵǴ� ������ ����
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
		if (con == 3 || vow == 3) // ���� 2
		{
			return false;
		}
		if (i > 0 && s[i - 1] == s[i] && !(s[i] == 'e' || s[i] == 'o')) // ���� 3
		{
			return false;
		}
	}
	if (!flag) // ���� 1
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