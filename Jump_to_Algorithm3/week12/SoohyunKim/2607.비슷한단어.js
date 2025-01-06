const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(input) {
  const n = input.shift(); 
  const target = input.shift().split('');
  const targetMap = getCharCount(target);
  let answer = 0;

  for (let word of input) {
    const wordArr = word.split('');
    const wordMap = getCharCount(wordArr);

    // 차이가 1 이내인지 확인
    const diff = getDiffCount(targetMap, wordMap);
    if (diff <= 1) answer++;
  }

  return answer;
}

function getCharCount(word) {
  const map = new Map();
  for (const char of word) {
    map.set(char, (map.get(char) || 0) + 1);
  }
  return map;
}

function getDiffCount(map1, map2) {
  let diff = 0;

  for (const [key, value] of map1) {
    diff += Math.abs(value - (map2.get(key) || 0));
  }

  for (const [key, value] of map2) {
    if (!map1.has(key)) diff += value;
  }

  return diff;
}

console.log(solution(input));