const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(input) {
  const [N, M, X] = input[0].split(' ').map(Number);
  const roads = input.slice(1).map((line) => line.split(" ").map(Number));

  const graph = Array.from({ length: N + 1 }, () => []);
  const reverseGraph = Array.from({ length: N + 1 }, () => []);

  for (const [from, to, time] of roads) {
    graph[from].push([to, time]);
    reverseGraph[to].push([from, time]);
  }

  const toX = dijkstra(X, reverseGraph, N);
  const fromX = dijkstra(X, graph, N);

  let maxTime = 0;

  for (let i = 1; i <= N; i++) {
    maxTime = Math.max(maxTime, toX[i] + fromX[i]);
  }

  return maxTime;
}

function dijkstra(start, graph, N) {
  const distances = Array(N + 1).fill(Infinity);
  const visited = Array(N + 1).fill(false);
  distances[start] = 0;

  const priorityQueue = [[0, start]];

  while (priorityQueue.length) {
    priorityQueue.sort((a, b) => b[0] - a[0]); 
    const [currentDist, currentNode] = priorityQueue.pop();

    if (visited[currentNode]) continue;
    visited[currentNode] = true;

    for (const [nextNode, weight] of graph[currentNode]) {
      const newDist = currentDist + weight;

      if (newDist < distances[nextNode]) {
        distances[nextNode] = newDist;
        priorityQueue.push([newDist, nextNode]);
      }
    }
  }

  return distances;
}

console.log(solution(input));