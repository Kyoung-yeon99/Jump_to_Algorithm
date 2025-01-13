const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(input) {
  const [N, M] = input[0].split(' ').map(Number);
  const measure = [];

  // 전투력 측정 기준 저장
  for (let i = 1; i <= N; i++) {
    const [name, power] = input[i].split(' ');
    measure.push([name, +power]);
  }

  // 캐릭터 전투력 배열
  const characters = input.slice(N + 1).map(Number);

  let answer = [];
  const powers = measure.map(([, power]) => power); // 전투력만 추출

  for (let i = 0; i < M; i++) {
    let left = 0;
    let right = N - 1;

    // 이분 탐색
    while (left <= right) {
      const mid = Math.floor((left + right) / 2);
      if (powers[mid] >= characters[i]) {
        answer[i] = measure[mid][0];  
        right = mid - 1; 
      } else {
        left = mid + 1; 
      }
    }
  }

  return answer.join('\n');
}

console.log(solution(input));