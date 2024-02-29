#include <bits/stdc++.h>
using namespace std;

pair<char, char> arr[26]; //각 알파펫 노드로 (left, right) 정보 저장
int N;

void preorder(char x)
{
	if (x != '.')
	{
		//전위 순회는 루트(x)가 먼저 출력되어야 함
		cout << x;
		preorder(arr[x - 'A'].first);
		preorder(arr[x - 'A'].second);
	}
}

void inorder(char x)
{
	if (x != '.')
	{
		//후위 순회는 루트(x)가 중간에 출력되어야 함
		inorder(arr[x - 'A'].first);
		cout << x;
		inorder(arr[x - 'A'].second);
	}
}
void postorder(char x)
{
	if (x != '.')
	{
		//후위 순회는 루트(x)가 맨 마지막에 출력되어야 함
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

	//A부터 순회시작
	preorder('A');
	cout << endl;
	inorder('A');
	cout << endl;
	postorder('A');
}