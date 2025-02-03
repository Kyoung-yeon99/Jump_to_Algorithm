const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');


function solution(input) {
  const [N, M] = input.shift().split(' ').map(Number);
  const map = input.map(row => row.split(' ').map(Number));

  // 치킨, 집 좌표 저장
  const chickenPos = [];
  const housePos = [];
  for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
          if (map[i][j] === 2) chickenPos.push([i, j]);
          if (map[i][j] === 1) housePos.push([i, j]);
      }
  }

  const isUsed = []; //치킨집
  const comb = []; //조합
  const answer = []; //치킨거리 합
  // 치킨 거리를 계산하는 함수
  const distanceCheck = (x, y) => {
      return Math.abs(x[0] - y[0]) + Math.abs(x[1] - y[1]);
  };

  const dfs = (depth) => {
      if (depth === M) {
          let sumDistance = 0;
          for (let house of housePos) {
              let minDistance = Infinity;
              for (let chicken of comb) {
                  minDistance = Math.min(distanceCheck(house, chicken), minDistance);
              }
              sumDistance += minDistance;
          }
          answer.push(sumDistance);
          return;
      }

      for (let i = 1; i <= chickenPos.length; i++) {
          if (!isUsed[i]) {
              if (
                  depth > 0 &&
                  (comb[depth - 1][0] > chickenPos[i - 1][0] ||
                  (comb[depth - 1][0] === chickenPos[i - 1][0] &&
                  comb[depth - 1][1] > chickenPos[i - 1][1]))
              ) continue;

              comb[depth] = chickenPos[i - 1];
              isUsed[i] = true;
              dfs(depth + 1);
              isUsed[i] = false;
          }
      }
  };

  dfs(0);
  return Math.min(...answer);
}

console.log(solution(input));