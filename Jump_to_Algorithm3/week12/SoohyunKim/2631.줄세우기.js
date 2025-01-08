const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(input) {
  const N = +input.shift();
  const arr = input.map((i) => +i);
  const longest = new Array(N).fill(1);

  // LIS 계산
  for (let i = 1; i < N; i++) {
    let cnt = 0;
    for (let j = 0; j < i; j++) {
      if (arr[j] < arr[i]) 
        cnt = Math.max(cnt, longest[j]);
    }
    longest[i] = cnt + 1;
  }

  return N - Math.max(...longest);
}

console.log(solution(input));