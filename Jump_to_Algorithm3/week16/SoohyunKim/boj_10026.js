const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const N = +input.shift();
const graph = input.map(row => row.split(''));
dir = [[0, 1], [0, -1], [1, 0], [-1, 0]];

let normalCount = 0, blindCount = 0;
  
let visitedNormal = Array.from({ length: N }, () => Array(N).fill(false));
let visitedBlind = Array.from({ length: N }, () => Array(N).fill(false));

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (!visitedNormal[i][j]) {
      bfs(i, j, graph[i][j], visitedNormal, false);
      normalCount++;
    }
    if (!visitedBlind[i][j]) {
      bfs(i, j, graph[i][j], visitedBlind, true);
      blindCount++;
    }
  }
}
console.log(`${normalCount} ${blindCount}`);

function bfs(x, y, color, visited, isBlind) {
  let queue = [[x, y]];
  visited[x][y] = true;

  while (queue.length > 0) {
    let [cx, cy] = queue.shift();

    for (let [dx, dy] of dir) {
      let nx = cx + dx;
      let ny = cy + dy;

      if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny]) {
        // 적록색약 => R, G 같은 색
        if (isBlind) {
          if ((color === "R" || color === "G") && (graph[nx][ny] === "R" || graph[nx][ny] === "G")) {
            visited[nx][ny] = true;
            queue.push([nx, ny]);
          } else if (color === "B" && graph[nx][ny] === "B") {
            visited[nx][ny] = true;
            queue.push([nx, ny]);
          }
        }
        // 일반
        else {
          if (graph[nx][ny] === color) {
            visited[nx][ny] = true;
            queue.push([nx, ny]);
          }
        }
      }
    }
  }
}