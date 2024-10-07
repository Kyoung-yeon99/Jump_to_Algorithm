// 가로 w, 세로 h인 직사각형, 1x1 정사각형으로 자를 예정
// 근데, 대각선 방향으로 잘라놈.
// 크기가 같은 직각삼각형 2개로 나눠짐
// 이때 사용할 수 있는 1x1 정사각형 개수?

import java.math.*;

class Solution {
    public long solution(int w, int h) { // 1억 이하 자연수
        long answer = 1;

        // 꼭짓점에서 만나는 점(사각형 중복됨) -> 최대공약수로 빼주기
        // 전체 사각형 개수
        long total = (long) w * h; // 1억이니까 long형변환

        // w,h 최대공약수
        long gcd = BigInteger.valueOf(w).gcd(BigInteger.valueOf(h)).longValue();

        // 사용할 수 없는 정사각형
        long unuse = w + h - gcd;

        answer = total - unuse;

        return answer;
    }
}