class Solution {
    public int solution(String s) {
        // 입력된 문자열 s의 길이를 answer에 초기값으로 설정
        int answer = s.length();

        // 문자열의 절반 길이를 구함. 반복 압축은 최대 문자열 절반까지만 할 수 있음
        int HALF = s.length() / 2;

        // 문자열을 1부터 절반 길이까지 단위로 나누어 압축을 시도
        for (int i = 1; i <= HALF; i++) {
            // 처음 i 길이만큼 잘라서 slice로 저장
            String slice = s.substring(0, i);

            // compare 함수 호출하여 i 길이 단위로 압축한 문자열을 얻음
            String compare_str = compare(i, s, slice);

            // 압축한 문자열의 길이와 현재까지의 최소 길이를 비교하여 더 작은 값을 저장
            answer = Math.min(answer, compare_str.length());
        }

        // 최종적으로 가장 짧은 압축 문자열의 길이를 반환
        return answer;
    }

    // len: 비교할 문자열 단위 길이
    // s: 입력된 원본 문자열
    // slice: 현재 비교할 첫 번째 단위 문자열
    public String compare(int len, String s, String slice) {
        // 압축된 문자열을 저장할 변수
        String result = "";
        // 같은 단위 문자열이 반복되는 횟수
        int count = 1;

        // len 단위로 원본 문자열을 순회하며 비교
        for (int i = len; i < s.length(); i += len) {
            // 현재 비교할 문자열의 끝 범위를 구함
            int limit = i + len;
            // 범위가 문자열 길이를 넘을 수 있으므로 범위를 문자열 끝으로 조정
            if (i + len >= s.length()) {
                limit = s.length();
            }

            // slice와 비교할 대상 문자열
            String target = s.substring(i, limit);

            // 현재 slice와 target이 같으면 count를 증가
            if (slice.equals(target)) {
                count++;
            } else {
                // 같지 않다면 지금까지의 반복된 slice를 result에 추가
                if (count == 1) {
                    // count가 1이면 숫자를 생략하고 slice만 추가
                    result += slice;
                } else {
                    // count가 1보다 크면 count와 함께 slice를 추가
                    result += (count + slice);
                }
                // 다음 단위 문자열을 slice로 설정하고, count를 1로 초기화
                count = 1;
                slice = target;
            }
        }

        // 마지막 남은 slice를 처리 (반복 여부에 따라 다른 방식으로 추가)
        if (count == 1) {
            result += slice;
        } else {
            result += (count + slice);
        }

        // 최종 압축된 문자열 반환
        return result;
    }
}
