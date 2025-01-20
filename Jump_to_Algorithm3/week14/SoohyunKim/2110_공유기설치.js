const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(input) {
  const [ N, C ] = input.shift().split(' ').map(Number);
  const houses = input.map(row => Number(row));
  houses.sort((a, b) => a - b);

  let start = 1;
  let end = houses[N-1];

  while (start <= end) {
    const mid = Math.floor((start + end) / 2);

    let count = 1;
    let prev = houses[0];

    for(const cur of houses){
      if (cur - prev < mid) continue;
      prev = cur;
      count += 1;
    }

    if (count < C) end = mid - 1;
    else start = mid + 1;
  }
  return end;
}

console.log(solution(input));