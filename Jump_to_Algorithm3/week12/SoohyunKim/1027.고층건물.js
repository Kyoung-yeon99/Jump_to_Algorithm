const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(input) {
  const N = +input[0];
  const buildings = input[1].split(' ').map(Number);
  let answer = 0;

  // 기울기 계산
  const slope = (x1, y1, x2, y2) => {
    return (y2 - y1) / (x2 - x1);
  }

  for (let i = 0; i < N; i++) {
    // 현재 건물 좌표
    const x1 = i + 1; 
    const y1 = buildings[i]; 

    // 오른쪽
    let maxRight = null;  // 가장 큰 기울기
    let visibleRight = 0; // 볼 수 있는 빌딩 수

    for (let j = i + 1; j < N; j++) {
      const x2 = j + 1;
      const y2 = buildings[j];
      const slopeRight = slope(x1, y1, x2, y2);

      // 기울기가 커지는 경우 -> 보인다
      if (maxRight === null || maxRight < slopeRight) {
        maxRight = slopeRight;
        visibleRight++;
      }
    }

    // 왼쪽
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

    if ((visibleLeft + visibleRight) > answer) {
      answer = visibleLeft + visibleRight;
    }
  }
  
  return answer;
}

console.log(solution(input));