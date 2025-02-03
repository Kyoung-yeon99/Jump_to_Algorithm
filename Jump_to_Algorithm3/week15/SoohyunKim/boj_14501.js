const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(input) {
  const N = Number(input.shift());
  const counsel = input.map(v => v.split(' ').map(Number)); // 상담 일정
  const maxProfit = new Array(N + 1).fill(0); // 최대 수익을 저장하는 DP 배열

  for (let i = 0; i < N; i++) {
    const [time, profit] = counsel[i];

    // 현재까지의 최댓값
    if (i > 0) maxProfit[i] = Math.max(maxProfit[i], maxProfit[i - 1]);

    // 상담을 진행할 수 있는 경우
    if (i + time <= N) {
      maxProfit[i + time] = Math.max(maxProfit[i + time], maxProfit[i] + profit);
    }
  }

  return Math.max(...maxProfit);
}

console.log(solution(input));