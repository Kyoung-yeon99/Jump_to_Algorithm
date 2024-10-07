import java.util.*;

class Solution {
    public int solution(String dirs) {
        // 경로의 중복을 제거하고 유일한 경로를 저장하기 위한 HashSet
        HashSet<String> set = new HashSet<>();

        // 현재 위치를 나타내는 좌표
        int nowY = 0;
        int nowX = 0;
        // 이전 위치를 나타내는 좌표
        int prevY = 0;
        int prevX = 0;

        // 주어진 명령 문자열을 하나씩 처리
        for (int i = 0; i < dirs.length(); i++) {
            char ch = dirs.charAt(i);

            // 명령에 따라 방향을 설정 ('U': 위, 'D': 아래, 'R': 오른쪽, 'L': 왼쪽)
            switch (ch) {
                case 'U': // 위로 이동
                    nowY--;
                    break;
                case 'D': // 아래로 이동
                    nowY++;
                    break;
                case 'R': // 오른쪽으로 이동
                    nowX++;
                    break;
                case 'L': // 왼쪽으로 이동
                    nowX--;
                    break;
            }

            // 좌표가 범위를 벗어나면 (좌표 범위는 -5 <= x, y <= 5) 이동 취소
            if (nowY < -5 || nowX < -5 || nowY > 5 || nowX > 5) {
                // 현재 좌표를 이전 좌표로 되돌리고 continue로 다음 명령으로 넘어감
                nowY = prevY;
                nowX = prevX;
                continue;
            }

            // 현재 좌표와 이전 좌표를 배열로 저장
            int arr[][] = {{nowY, nowX}, {prevY, prevX}};

            // 경로를 저장하기 위해 두 좌표를 정렬 (순서를 일관되게 맞추기 위해 정렬 사용)
            Arrays.sort(arr, new Comparator<>() {
                @Override
                public int compare(int arr1[], int arr2[]) {
                    // 첫 번째 값이 크면 뒤로 보냄
                    if (arr1[0] > arr2[0])
                        return 1;
                        // 첫 번째 값이 같으면 두 번째 값으로 비교
                    else if (arr1[0] == arr2[0]) {
                        if (arr1[1] > arr2[1]) return 1;
                    }
                    return -1;
                }
            });

            // 정렬된 좌표를 문자열로 변환해 HashSet에 추가 (경로 중복 제거를 위해)
            set.add(arr[0][0] + " " + arr[0][1] + " " + arr[1][0] + " " + arr[1][1]);

            // 이전 좌표를 현재 좌표로 갱신
            prevY = nowY;
            prevX = nowX;
        }

        // 유일한 경로의 개수를 반환
        return set.size();
    }
}
