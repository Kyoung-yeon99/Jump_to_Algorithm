const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(input) {
  const n = input.shift();
  const target = input.shift();
  let answer = 0;

  for (let word of input) {
    if (
      Math.abs(target.length - word.length) > 1 ||
      Math.abs(new Set(target).size - new Set(word).size) > 1 // 단어중복제거
    )
      continue;

    for (const char of target) 
      word = word.replace(char, ''); // 일치되는 문자 제거
    
    if (word.length < 2) 
      answer++;
  }

  return answer;
}

console.log(solution(input));