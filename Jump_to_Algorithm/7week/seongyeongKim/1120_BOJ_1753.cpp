/*
������ Ǯ��: https://wooono.tistory.com/398
*/

#include <bits/stdc++.h>
using namespace std;

#define INF 1000000 // ���� ��忡�� �ش� �������� ��ΰ� ���� ����� ���
#define MAX_VERTEX 20001 // �ִ� vertex ����
#define MAX_EDGE 300001 // �ִ� edge ����

// �ּ� ��� �迭
int d[MAX_VERTEX];

// ���� ������ ���� Vector ����
// index : ���� ���
// value : pair<���, ���� ���> ���
vector<pair<int, int> > edge[MAX_EDGE];

void dijkstra(int start_node) {

    // ���� ��忡�� ���� ���� ���� ����� 0
    d[start_node] = 0;

    // ���� ������ � ���� �������� �ּ� ����� �����ϴ� ���� ����̸�,
    // pair<���, ���� ���> ������ �켱 ���� ť�̴�.
    priority_queue<pair<int, int> > pq;

    // ���� ��忡�� ���� ���� ���� ��ο� ����� pq �� ����
    pq.push(make_pair(0, start_node));

    // pq �� ��� ��ε��� Ȯ���� ������ �ݺ�
    while (!pq.empty()) {

        // ������ �켱 ���� ť��, ù ��° ���� �������� ū ���� top �� ������ ���ĵǾ��ִ�.
        // ������, �ش� �˰��򿡼�, ��� ���� ����ȭ �� �� ù ��° ������ �����ϰ�, ���� ���� �� ��° ������ �����Ѵ�.
        // ����, ����� ���� ���� ���� top �� ������ ���ĵǾ��ִ�.
        // ��, ���� �ּ� ����� �����ϴ� ��κ��� Ȯ���ϰ� �ȴ�.

        // ���� ��忡�� � ���� �������� �ּ� ��θ� �����ϴ� pq �� top ����,
        // ���� ��带 ���� ���� �����Ѵ�.
        int current = pq.top().second;

        // ���� ��忡�� ���� �������� ����� �����Ѵ�.
        // ����� ����ȭ�Ǿ��ִ� �����̹Ƿ�, ���ȭ�ؼ� ����Ѵ�.
        int start_to_current_distance = -pq.top().first;

        // ���� ��δ� Ȯ�� �Ǿ����Ƿ�, �켱 ���� ť���� �����Ѵ�.
        pq.pop();

        // pq �� top ���� ����, ���� ������ ���� �������� ����
        // �ּ� ��� �迭�� �ִ�, ���� ������ ���� �������� ����� �������ν�,
        // pq �� top ���� ����, ���� ������ ���� �������� ����� �� ũ��
        // ���� �ش� ��θ� ���� ������ ������ Ȯ���� �ʿ䰡 �����Ƿ�, �� �̻� Ȯ������ ����
        if (d[current] < start_to_current_distance) {
            continue;
        }

        // ��� ���ǹ��� �ɸ��� �ʰ� ����ϸ�,
        // ���� ������ ���� �������� �ּ� ������� �̷���� �����̹Ƿ�, 
        // ���� ���� ���� ����� ������ ��� �˻��Ѵ�.
        for (int i = 0; i < edge[current].size(); ++i) {

            // ���� ��� ����
            // ��, ���� ���� i ��°�� ������ ���
            int next = edge[current][i].second;

            // ���� ��忡�� ���� �������� ��� ����
            // ��, ���� ��忡�� ���� �������� ��� + ���� ��忡�� i ��°�� ������ �������� ���
            int start_to_next_distance = start_to_current_distance + edge[current][i].first;

            // ������, ���� ��忡�� ���� �������� �ּ� ��뺸��
            // ���Ӱ� �����, ���� ��忡�� ���� �������� ����� �� �۴ٸ�
            // �ּ� ����� ������Ʈ
            if (d[next] > start_to_next_distance) {
                d[next] = start_to_next_distance;

                // ����, ���ŵ� ��ΰ� �ּ� ������� �����ϱ� ����
                // �켱 ���� ť�� �ش� ��� ����
                pq.push(make_pair(-start_to_next_distance, next));
            }
        }
    }
}

int main() {

    // ����� ������ ������ ���� �Է�
    int v, e;
    cin >> v >> e;

    // ���� ��� �Է�
    int start_node;
    cin >> start_node;

    // �ּ� ��� �迭 �ʱ�ȭ
    for (int i = 1; i < v + 1; ++i) {
        d[i] = INF;
    }

    // ���� ����
    for (int i = 0; i < e; ++i) {

        // ���� ���, ���� ���, ��� �Է�
        int start, end, cost;
        cin >> start >> end >> cost;

        // ���� ��忡 ���� <���, ���� ���> ����
        edge[start].push_back(make_pair(cost, end));
    }

    // ���ͽ�Ʈ�� �Լ� ����
    dijkstra(start_node);

    // �ּ� ��� �迭 ���
    for (int i = 1; i < v + 1; ++i) {
        if (d[i] == INF) {
            cout << "INF" << " ";
        }
        else {
            cout << d[i] << " ";
        }
    }

    return 0;

}