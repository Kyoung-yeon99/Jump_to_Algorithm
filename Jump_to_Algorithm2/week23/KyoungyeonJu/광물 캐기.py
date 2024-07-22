def solution(picks, minerals):
    d = {'diamond': 0, 'iron': 1, 'stone': 2}
    score = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]

    sum_picks = sum(picks)
    if len(minerals) > sum_picks*5:  # 광물 개수가 총 곡괭이 수의 5배보다 많은 경우
        minerals = minerals[:sum_picks*5]

    # 광물들을 5개씩 묶어서, 다이아몬드, 철, 돌의 개수 구하기
    cnt = [[0, 0, 0] for _ in range(sum_picks)]
    for i in range(len(minerals)):
        m = d[minerals[i]]
        cnt[i//5][m] += 1

    sorted_cnt = sorted(cnt, key=lambda x:(-x[0], -x[1], -x[2]))  # 내림차순 정렬

    # 가지고 있는 곡괭이 중 다,철, 돌 순의 개수로 피로도
    answer = 0
    for row in sorted_cnt:
        diamond, iron, stone = row
        for p in range(len(picks)):
            if p == 0 and picks[0] > 0:
                answer += diamond + iron + stone
                picks[0] -= 1
                break
            elif p == 1 and picks[1] > 0:
                answer += diamond*5 + iron + stone
                picks[1] -= 1
                break
            elif p == 2 and picks[2] > 0:
                answer += diamond*25 + iron*5 + stone
                picks[2] -= 1
                break

    return answer

