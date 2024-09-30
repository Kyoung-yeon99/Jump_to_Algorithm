public class Solution {
    int[] answer;

    public void quadZip(int[][] arr, int x, int y, int length) {
        // 현재 영역이 압축 가능하면 answer 배열에 값 추가하고 반환
        if (zipChk(arr, x, y, length, arr[x][y])) {
            if (arr[x][y] == 1) answer[1]++;
            else answer[0]++;
            return;
        }

        // 1번 영역
        quadZip(arr, x, y, length / 2);
        // 2번 영역
        quadZip(arr, x + length / 2, y, length / 2);
        // 3번 영역
        quadZip(arr, x, y + length / 2, length / 2);
        // 4번 영역
        quadZip(arr, x + length / 2, y + length / 2, length / 2);
    }

    public boolean zipChk(int[][] arr, int x, int y, int length, int arrVal) {
        for (int i = x; i < x + length; i++) {
            for (int j = y; j < y + length; j++) {
                // 영역의 첫번째 값과 나머지를 비교하다 다르면 반환
                if (arr[i][j] != arrVal) return false;
            }
        }
        return true;
    }

    public int[] solution(int[][] arr) {
        answer = new int[2];
        quadZip(arr, 0, 0, arr.length);
        return answer;
    }
}