const stdin = require('fs').readFileSync('/dev/stdin').toString().trim();
const input = stdin.split('\n').map(v => v.split(' ').map(Number));
const [N, A, operators] = input;

let max = -1_000_000_000;
let min = 1_000_000_000;

const calculate = [
  (a, b) => a + b,
  (a, b) => a - b,
  (a, b) => a * b,
  (a, b) => ~~(a / b),
];

const dfs = (count = 0, result = A[0]) => {
  if (count === N - 1) {
    max = Math.max(max, result);
    min = Math.min(min, result);
  } else {
    for (let i = 0; i < 4 ; i++) {
      if (!operators[i]) {
        continue;
      }
      operators[i]--;
      dfs(count + 1, calculate[i](result, A[count + 1]));
      operators[i]++;
    }
  }
}
dfs();
  
console.log(max);
console.log(min);