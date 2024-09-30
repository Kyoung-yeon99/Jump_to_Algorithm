
// 문자열 {, } 자르기

import java.util.*;

class Solution {
    public ArrayList<Integer> solution(String s) {
        // int[] answer = {};
        ArrayList<Integer> answer = new ArrayList<>();

        s = s.substring(1, s.length() - 1); // 양 옆 { } 자르기
        // System.out.println(s); // 확인용

        String arr[] = s.split("},");
        int len = arr.length;

        // 체크
        for (int i = 0; i < arr.length; i++) {
            arr[i] = arr[i].substring(1, arr[i].length());
            // System.out.println(arr[i]);
        }
        arr[len - 1] = arr[len - 1].substring(0, arr[len - 1].length() - 1); //맨 마지막 } 제거
        // System.out.println(arr[len-1]);

        // 문자열 길이 기준 오름차순 정렬
        Arrays.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                return s1.length() - s2.length();
            }
        });

        for (String a : arr) {
            String tmp[] = a.split(",");
            for (String t : tmp) {
                // System.out.println(t);
                int num = Integer.parseInt(t);
                if (!answer.contains(num)) {
                    answer.add(num);
                }
            }
            // System.out.println();
        }
        return answer;
    }
}