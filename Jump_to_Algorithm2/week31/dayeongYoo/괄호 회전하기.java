// 여러가지 괄호가 섞인 문자열을 입력값
// 이 괄호를  문자열의 길이만큼 회전시키고,  회전시킨값이 '올바른 괄호 문자열'이라면,
// 결과값을 +1 늘리기

import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        String str = s;

        for (int i = 0; i < s.length(); i++) {
            char temp = str.charAt(0);
            str = str.substring(1) + temp;
            if (isCorrect(str)) {
                answer++;
            }
        }

        return answer;
    }

    public boolean isCorrect(String str) {
        Stack<Character> s = new Stack<>();

        char[] arr = str.toCharArray();

        for (char data : arr) {
            if (s.isEmpty()) {
                s.push(data);
            } else if (s.peek() == '[' && data == ']') {
                s.pop();
            } else if (s.peek() == '(' && data == ')') {
                s.pop();
            } else if (s.peek() == '{' && data == '}') {
                s.pop();
            } else {
                s.push(data);
            }
        }

        if (s.isEmpty()) {
            return true;
        }

        return false;
    }
}
