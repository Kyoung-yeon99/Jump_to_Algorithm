
public class Solution {

    public static void main(String[] args) {
        // Solution 클래스의 인스턴스를 생성하고 테스트 케이스 실행
        Solution s = new Solution();
        String skill = "CBD";  // 스킬 순서 "CBD"
        String[] skill_trees = {"BACDE", "CBADF", "AECB", "BDA"};  // 검사할 스킬 트리 배열

        // solution 메소드 호출
        s.solution(skill, skill_trees);
    }

    public int solution(String skill, String[] skill_trees) {
        int answer = 0;  // 유효한 스킬 트리의 개수를 저장하는 변수
        boolean[] alphabet = new boolean[26];  // 각 알파벳이 스킬에 포함되어 있는지 여부를 저장하는 배열

        // skill 문자열을 순회하여 스킬에 포함된 알파벳을 true로 설정
        for (int i = 0; i < skill.length(); i++) {
            alphabet[skill.charAt(i) - 'A'] = true;
        }

        // 각 스킬 트리마다 검사
        for (String trees : skill_trees) {
            StringBuilder sb = new StringBuilder();  // 스킬 순서만 추출할 StringBuilder

            // 스킬 트리의 각 문자에 대해 스킬에 포함된 문자만 추출
            for (int i = 0; i < trees.length(); i++) {
                if (alphabet[trees.charAt(i) - 'A']) {
                    sb.append(trees.charAt(i));  // 포함된 문자는 StringBuilder에 추가
                }
            }

            // 추출된 스킬 순서가 유효한지 검사 (compare 메소드 호출)
            if (compare(sb, skill)) {
                answer++;  // 유효한 스킬 트리일 경우 카운트 증가
            }
        }

        return answer;  // 유효한 스킬 트리의 총 개수를 반환
    }

    // 추출된 스킬 순서가 주어진 스킬 순서와 맞는지 비교하는 메소드
    private boolean compare(StringBuilder sb, String skill) {
        // 추출된 스킬 순서의 각 문자와 주어진 스킬 순서의 문자를 비교
        for (int i = 0; i < sb.toString().length(); i++) {
            if (sb.toString().charAt(i) != skill.charAt(i)) {
                return false;  // 순서가 맞지 않으면 false 반환
            }
        }

        return true;  // 순서가 맞으면 true 반환
    }
}
