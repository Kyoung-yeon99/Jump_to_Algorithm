const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(input) {
  const [N, d, k, c] = input.shift().split(' ').map(Number);
  const sushi = input.map(row => Number(row));
  let check = Array(d + 1).fill(0); // 각 초밥 먹은 개수 세기 위한 배열
  let cnt = 0; // 현재까지 먹은 초밥 종류
  let answer = 0; // 최대 초밥 종류

  // 첫 번째 구간 계산
  for (let i = 0; i < k; i++) {
    if (check[sushi[i]] == 0) {
      cnt++;
    }
  
    check[sushi[i]]++;
  }
  answer = cnt;

  // 슬라이딩 윈도우, 다른 구간 탐색
  for (let s = 0; s < N; s++) {
    let end = (s + k) % N; // 끝지점
  
    if (cnt >= answer) {
      if (check[c] == 0) { // 쿠폰 초밥 없음
        answer = cnt + 1;
      } else {
        answer = cnt;
      }
    }
  
    // 슬라이딩 윈도우 이동
    check[sushi[s]]--; 
    if (check[sushi[s]] == 0) cnt--; // 스시 가짓수 업데이트
    
    if (check[sushi[end]] == 0) cnt++;
    check[sushi[end]]++;
  }

  return answer;
}

console.log(solution(input));