#include <bits/stdc++.h>
using namespace std;

pair<char, char> arr[26]; //�� ������ ���� (left, right) ���� ����
int N;

void preorder(char x)
{
	if (x != '.')
	{
		//���� ��ȸ�� ��Ʈ(x)�� ���� ��µǾ�� ��
		cout << x;
		preorder(arr[x - 'A'].first);
		preorder(arr[x - 'A'].second);
	}
}

void inorder(char x)
{
	if (x != '.')
	{
		//���� ��ȸ�� ��Ʈ(x)�� �߰��� ��µǾ�� ��
		inorder(arr[x - 'A'].first);
		cout << x;
		inorder(arr[x - 'A'].second);
	}
}
void postorder(char x)
{
	if (x != '.')
	{
		//���� ��ȸ�� ��Ʈ(x)�� �� �������� ��µǾ�� ��
		postorder(arr[x - 'A'].first);
		postorder(arr[x - 'A'].second);
		cout << x;
	}
}
int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N;
	for (int i = 0; i < N; i++)
	{
		char parent, left, right;
		cin >> parent >> left >> right;

		arr[(parent - 'A')].first = left;
		arr[(parent - 'A')].second = right;
	}

	//A���� ��ȸ����
	preorder('A');
	cout << endl;
	inorder('A');
	cout << endl;
	postorder('A');
}