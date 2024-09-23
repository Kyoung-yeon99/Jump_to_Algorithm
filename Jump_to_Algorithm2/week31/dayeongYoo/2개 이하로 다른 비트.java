// 짝수: 마지막 비트 0 -> 바로 다음 숫자가 답 : 2(10) 다음수 3(11)-> 비트 1개 다름
// 홀수: 마지막 비트 1 -> 첫번째로 만나는 0을 1로 바꾸고, 그다음 자리를 0으로 바꾸면 답
// https://velog.io/@anwlro0212/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-2%EA%B0%9C-%EC%9D%B4%ED%95%98%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EB%B9%84%ED%8A%B8-JAVA

class Solution {
    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];

        for (int i = 0; i < numbers.length; i++) {
            String word = Long.toString(numbers[i], 2);
            word = "0" + word; //만약 1111이 입력인 경우에는 단 1개도 0으로 바꿀 수 없음.
            int idx1 = -1;
            int idx2 = -1;

            for (int j = word.length() - 1; j >= 0; j--) { //오른쪽에서부터 가장 가까운 0의 인덱스를 찾음
                if (word.charAt(j) - '0' == 0) {
                    idx1 = j;
                    break;
                }
            }

            for (int j = idx1 + 1; j < word.length(); j++) { //0의 인덱스보다 1 높은 인덱스부터 가장 가까운 1을 찾음
                if (word.charAt(j) - '0' == 1) {
                    idx2 = j;
                    break;
                }
            }

            StringBuilder sb = new StringBuilder(word);
            sb.setCharAt(idx1, '1'); //0을 발견한 곳을 1로 바꿔줌.
            if (idx2 != -1) { // 1을 발견 못했다면 처리 X. 발견했다면 0으로 바꿔줌
                sb.setCharAt(idx2, '0');
            }

            answer[i] = Long.parseLong(sb.toString(), 2); //10진법으로 변환
        }

        return answer;
    }
}