const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(input) {
  const str = input[0];
  const target = input[1];
  const len = target.length;
  const stack = [];

  for (let i = 0; i < str.length; i++) {
    stack.push(str[i]); // 스택 추가
  
    // 마지막 문자가 target과 일치할 경우
    if (stack.length >= len && stack.slice(-len).join('') === target) {
      stack.splice(-len, len); // 폭발 문자열 제거
    }
  }
  const result = stack.join("");
  return result === "" ? "FRULA" : result;
}

console.log(solution(input));