const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const V = +input[0];
const graph = Array.from({ length: V + 1 }, () => []);

for (let i = 1; i <= V; i++) {
    const data = input[i].split(' ').map(Number);
    const node = data[0]; // 정점

    for (let j = 1; j < data.length - 1; j += 2) {
        const neighbor = data[j]; // 정점
        const cost = data[j + 1]; // 거리
        graph[node].push([neighbor, cost]);
    }
}

function bfs(start) {
    const dist = Array(V + 1).fill(-1); // 거리 정보
    const queue = [[start, 0]];
    dist[start] = 0;
    let farthestNode = start;
    let maxDist = 0;

    while (queue.length) {
        const [cur, curDist] = queue.shift();

        for (const [next, cost] of graph[cur]) {
            if (dist[next] === -1) {  // 방문하지 않은 노드
                dist[next] = curDist + cost;
                queue.push([next, dist[next]]);

                if (dist[next] > maxDist) {
                    maxDist = dist[next];
                    farthestNode = next;
                }
            }
        }
    }

    return [farthestNode, maxDist];
}

// 임의의 노드에서 가장 먼 노드를 찾는다.
const [farthestNode] = bfs(1);

// 가장 먼 노드에서 시작하여 트리의 지름을 구한다.
const [, answer] = bfs(farthestNode);

console.log(answer);