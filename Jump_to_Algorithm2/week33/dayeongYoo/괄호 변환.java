// (, )의 개수 같다면: "균형"
// (, )의 짝이 모두 맞다면: "올바른"
// 괄호 담는 자료구조 -> FIFO: queue 이용
// 다음 과정을 통해 균형 -> 올바른(짝이 맞도록) 으로 변환
//
class Solution {
    public String solution(String p) {
        String answer = "";

        if (p.isEmpty()) return ""; // isEmpty(): 문자열의 길이가 0인지 체크
        // 2. 문자열 w을 균형 문자열 u,v로 분리
        int balPoint = findSepa(p);
        String u = p.substring(0, balPoint);
        String v = p.substring(balPoint);

        // 3. 문자열 u가 올바른 이라면 v에 대해 1단계부터 다시 시행
        if (isCor(u)) {
            // 3-1. 수행한 결과 문자열을 u에 붙여 반환
            return u + solution(v);
        } else { // 4.
            StringBuilder sb = new StringBuilder();
            // 4-1.
            sb.append("(");
            // 4-2.
            sb.append(solution(v));
            // 4-3.
            sb.append(")");
            // 4-4.
            if (u.length() > 2) {
                for (int i = 1; i < u.length() - 1; i++) { // 1st, 마지막 문자 제거
                    sb.append(u.charAt(i) == '(' ? ')' : '(');
                }
            }
            return sb.toString();
        }
    }

    // 균형 잡힌 문자열의 분리점을 찾는 함수
    public int findSepa(String str) {
        int cnt = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '(') cnt++;
            else cnt--;
            if (cnt == 0) return i + 1; // 0일때 이때 분리해야 됨(idx+1)
        }
        return str.length(); //이미 균형 잡혀 있는 경우(매개변수는 균형문자열임)
    }

    // 균형 문자열인지 체크하는 함수-개수 같은지만 카운트
    public boolean isBal(String str) {
        int cnt = 0;
        for (char c : str.toCharArray()) {
            if (c == '(') cnt++;
            else if (c == ')') cnt--;
        }
        return cnt == 0; // 0이라면 균형 문자열:true, 아님 false
    }

    // 올바른 문자열인지 체크하는 함수-짝이 맞는지도 카운트
    public boolean isCor(String str) {
        int cnt = 0;
        for (char c : str.toCharArray()) {
            if (c == '(') cnt++;
            else if (c == ')') cnt--;
            if (cnt < 0) return false; // )가 (보다 먼저 나왔다면 그 즉시 fail 반환
        }
        return cnt == 0; // 0이라면 올바른 문자열:true, 아님 false
    }
}