const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M] = input.shift().split(' ').map(Number);
const graph = input.map(row => row.split(' ').map(Number));
const visited = Array.from(Array(N), () => Array(M).fill(false));

const dx = [0, 0, -1, 1];
const dy = [1, -1, 0, 0];

function bfs(x, y) {
  let count = 1;
  let queue = [[x, y]];
  visited[x][y] = true;

  while (queue.length) {
    const [cx, cy] = queue.pop();

    for (let i = 0; i < 4; i++) {
      const nx = cx + dx[i];
      const ny = cy + dy[i];

      if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx][ny] && graph[nx][ny] === 1) {
        visited[nx][ny] = true;
        queue.push([nx, ny]);
        count++;
      }
    }
  }
  return count;
}

let pictureCount = 0;
let maxSize = 0;

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (!visited[i][j] && graph[i][j] === 1) {
      pictureCount++;
      maxSize = Math.max(maxSize, bfs(i, j));
    }
  }
}

console.log(pictureCount);
console.log(maxSize);