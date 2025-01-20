const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(input) {
  const [N, M] = input.shift().split(' ').map(Number);
  const memo = new Set(input.slice(0, N));
  const blog = input.slice(N).map(row => row.split(','));
  let answer = [];

  for (let i = 0; i < M; i++) {
    for (const keyword of blog[i]) {
      memo.delete(keyword);
    }
    answer.push(memo.size);
  }

  return answer.join('\n');
}

console.log(solution(input));