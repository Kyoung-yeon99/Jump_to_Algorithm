#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9 + 7;
//0 - 정상적인 단방향 그래프 (node -> X)
//1 - 방향이 뒤집힌 그래프 (X -> node)
vector<int> dist[2];
vector<pair<int, int>> graph[2][1001];
int n, m, x;

void dijkstra(int k) {
	dist[k][x] = 0;

	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
	q.push({ 0,x });

	while (!q.empty()) {
		int d = q.top().first;
		int now = q.top().second;
		q.pop();

		if (d > dist[k][now]) continue;

		for (int i = 0; i < graph[k][now].size(); i++) {
			int next = graph[k][now][i].second;
			int next_d = d + graph[k][now][i].first;

			if (next_d < dist[k][next]) {
				dist[k][next] = next_d;
				q.push({ next_d,next });
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n >> m >> x;

	for (int i = 0; i < m; i++) {
		int a, b, t; //시작점, 끝점, 소요시간
		cin >> a >> b >> t;
		graph[0][a].push_back({ t,b });
		graph[1][b].push_back({ t,a });
	}

	for (int i = 0; i <= n; i++) {
		dist[0][i] = INF;
		dist[1][i] = INF;
	}

	dijkstra(0);
	dijkstra(1);

	int result = 0;

	for (int i = 1; i <= n; i++) {
		result = max(result, dist[0][i] + dist[1][i]);
	}

	cout << result << '\n';


	return 0;
}