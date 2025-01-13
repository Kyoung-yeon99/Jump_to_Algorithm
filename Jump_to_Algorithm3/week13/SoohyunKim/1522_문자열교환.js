const input = require('fs').readFileSync('/dev/stdin').toString().trim();

function solution(input) {
  const N = input.length;
  const countA = [...input].filter(char => char === 'a').length;
  input += input.slice(0, countA - 1); // 순환 구조로 만들기
  let min = Infinity;

  for(let i = 0; i < N; i++) {
    const window = input.slice(i, i + countA);
    const countB = [...window].filter(char => char === 'b').length;
    min = Math.min(min, countB);
  }

  return min;
}

console.log(solution(input));