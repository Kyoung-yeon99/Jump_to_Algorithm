const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(n) {
  if (n === 1) return 1;
  if (n === 2) return 2;

  let dp = new Array(n + 1).fill(0);
  dp[1] = 1;
  dp[2] = 2;

  for (let i = 3; i <= n; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
  }

  return dp[n];
}

console.log(solution(input));