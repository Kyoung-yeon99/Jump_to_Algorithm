def solution(n, m, section):
    ans = 0
    end = 0  # 롤러의 끝

    for s in section:
        if s > end:  # 롤러가 아직 지나지 않음 -> 칠해야 함
            end = s + m - 1
            ans += 1
        else:  # 이미 칠함
            continue

    return ans