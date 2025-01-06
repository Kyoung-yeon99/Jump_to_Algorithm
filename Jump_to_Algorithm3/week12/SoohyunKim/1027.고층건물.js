const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const buildings = input[1].split(' ').map(Number);

function slope(x1, y1, x2, y2) {
  return (y2 - y1) / (x2 - x1);
}
let result = 0;

for (let i = 0; i < N; i++) {
   const x1 = i +1; // 현재 건물의 x 좌표
   const y1 = buildings[i]; // 현재 건물의 y 좌표

   // 오른쪽 볼 수 있는 빌딩 수
   let maxRight = null; // 가장 큰 기울기
   let visibleRight = 0; // 볼 수 있는 건물 수

   for (let j = i + 1; j < N; j++) {
      const x2 = j + 1;
      const y2 = buildings[j];
      const slopeRight = slope(x1, y1, x2, y2);

      if (maxRight === null || maxRight < slopeRight) {
         maxRight = slopeRight;
         visibleRight++;
      }
   }

   // 왼쪽 볼 수 있는 빌딩 수
   let maxLeft = null;
   let visibleLeft = 0;

   for (let k = i - 1; k >= 0; k--) {
      const x2 = k + 1;
      const y2 = buildings[k];
      const slopeLeft = slope(x1, y1, x2, y2);

      if (maxLeft === null || maxLeft > slopeLeft) {
         maxLeft = slopeLeft;
         visibleLeft++;
      }
   }

   // 가장 많은 visible 판별
   if ((visibleLeft + visibleRight) > result) {
      result = visibleLeft + visibleRight;
   }
}

console.log(result);