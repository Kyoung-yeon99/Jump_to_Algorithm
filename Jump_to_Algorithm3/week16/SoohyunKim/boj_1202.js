const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, K] = input[0].split(' ').map(Number);
const dia = input.slice(1, N+1).map(row => row.split(' ').map(Number));
const bag = input.slice(N + 1).map(Number);

// 무게 기준으로 오름차순 정렬
dia.sort((a, b) => a[0] - b[0]);
bag.sort((a, b) => a - b);

const prices = []; 
let totalValue = 0;
let idx = 0;


for (let i = 0; i < K; i++) {
  while (idx < N && dia[idx][0] <= bag[i]) {
    prices.push(dia[idx][1]); 
    idx++;
  }

  if (prices.length > 0) {
    prices.sort((a, b) => b - a); 
    totalValue += prices.shift(); 
  }
}

console.log(totalValue);