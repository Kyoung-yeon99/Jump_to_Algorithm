const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(input) {
  const [n, m] = input.shift().split(' ').map(Number);
  const map = input.map(row => row.split(' ').map(Number));

  // 상하좌우 방향
  const dx = [0, 0, -1, 1];
  const dy = [-1, 1, 0, 0];
  // 결과 배열
  const result = Array.from({ length: n }, () => Array(m).fill(-1));

  // 목표 위치 찾기, 갈 수 없는 곳 0으로
  let targetX, targetY;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (map[i][j] === 2) {
        targetX = i;
        targetY = j;
        result[i][j] = 0; // 목표 지점은 0으로
      } else if (map[i][j] === 0) {
        result[i][j] = 0; // 목표 지점은 0으로
      }
    }
  }

  // BFS
  const queue = [[targetX, targetY]];

  while (queue.length > 0) {
    const [x, y] = queue.shift();

    // 상하좌우 탐색
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (nx >= 0 && nx < n && ny >= 0 && ny < m && map[nx][ny] === 1 && result[nx][ny] === -1) {
        result[nx][ny] = result[x][y] + 1; // 현재 칸에서 1칸 이동한 거리
        queue.push([nx, ny]);
      }
    }
  }

  return result.map(row => row.join(' ')).join('\n');
}

console.log(solution(input));