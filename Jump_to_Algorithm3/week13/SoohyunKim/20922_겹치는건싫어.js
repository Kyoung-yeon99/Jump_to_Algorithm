const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(input) {
  const [N, K] = input[0].split(' ').map(Number);
  const arr = input[1].split(' ').map(Number);

  const intMap = {};
  let maxLength = 0;
  let i = 0;
  let j = 0;
  
  while (i <= j && j < N) {
    while (intMap[arr[j]] === K) {
      intMap[arr[i]]--;
      i++;
    }
    maxLength = Math.max(maxLength, j - i + 1);
    intMap[arr[j]] = (intMap[arr[j]] ?? 0) + 1;
    j++;
  }

  return maxLength;
}

console.log(solution(input));