class Solution {
    public int[] solution(int n) {
        // 세 방향 존재 -> 아래, 오른쪽, 대각선(x,y 둘다 감소)
        int x = -1; // 아래 이동은 x 좌표 감소
        int y = 0; // 오른쪽 이동은 y 좌표 증가
        int num = 1; // 삼각 달팽이 채우기 값
        // 삼각형
        int[][] tri = new int[n][n];
        // 삼각형의 크기 ( 1 ~ n 까지 합)
        int[] answer = new int[n * (n + 1) / 2];

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (i % 3 == 0) { // 아래
                    x++;
                } else if (i % 3 == 1) { // 오른쪽
                    y++;
                } else if (i % 3 == 2) { // 대각선
                    x--;
                    y--;
                }
                tri[x][y] = num++;
            }
        }
        // 결과 배열에 담기
        int index = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (tri[i][j] == 0) break;
                answer[index++] = tri[i][j];
            }
        }
        return answer;
    }
}