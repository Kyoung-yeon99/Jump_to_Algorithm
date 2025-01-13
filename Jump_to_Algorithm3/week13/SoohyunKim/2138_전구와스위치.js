const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

function solution(input) {
  const N = +input[0];
  const current = input[1].split('').map(Number); 
  const target = input[2].split('').map(Number); 

  // 스위치 눌러 전구 상태를 바꾸는 함수
  const reverse = (arr, index) => {
    for (let i = index - 1; i <= index + 1; i++) {
      if (i >= 0 && i < N) {
        arr[i] = 1 - arr[i];
      }
    }
  };

  // 최소 스위치 횟수를 계산
  const countSwitches = (initialState, pressFirst) => {
    const state = [...initialState];
    let count = 0;

    // 첫 번째 스위치를 누르는 경우
    if (pressFirst) {
      reverse(state, 0);
      count++;
    }

    // 두 번째 전구부터 끝까지 처리
    for (let i = 1; i < N; i++) {
      if (state[i - 1] !== target[i - 1]) {
        reverse(state, i);
        count++;
      }
    }

    // 목표 상태와 일치 여부 확인
    return state.every((e, i) => e === target[i]) ? count : -1;
  };

  // 0번 스위치를 누르지 않은 경우와 누른 경우 두가지 계산
  const firstOff = countSwitches(current, false);
  const firstOn = countSwitches(current, true);

  // 최소값 계산
  if (firstOff === -1 && firstOn === -1) {
    return -1;
  } else if (firstOff === -1) {
    return firstOn;
  } else if (firstOn === -1) {
    return firstOff;
  } else {
    return Math.min(firstOff, firstOn);
  }
}

console.log(solution(input));