def solution(h1, m1, s1, h2, m2, s2):
    def calculate(h, m, s):  # 0시 0분 0초부터 h시 m분 s초까지 겹치는 횟수 구하는 함수
        ha = (h%12) * 30 + (m/60) * 30 + (s/3600) * 30  # 360//12 = 30
        ma = m * 6 + (s/60) * 6  # 360//60 = 6
        sa = s * 6

        ans = -1  # 0시 0분 0초는 1번 겹치므로 -1
        # 현재 각도에서의 겹침, 0시 0분 0초일 경우, ans는 1
        if sa >= ma: ans += 1
        if sa >= ha: ans += 1

        ans += (h*60 + m)*2  # 기본적으로 1분당 초침은 시침과 분침 2번 만남
        ans -= h  # 59분 -> 00분 일 때 초침은 분침과 만나지 않음
        if h >= 12:  # 11시59분59초 -> 12시 일 때,  분침과 만나지 않고 12시에 1번만 만나는 걸로 처리
            ans -= 2

        print(f'ha = {ha} ma = {ma} sa = {sa} ans = {ans}')
        return ans

    answer = calculate(h2, m2, s2) - calculate(h1, m1, s1)
    # 시작 시간이 0시와 12시인 경우, 예외적으로 1씩 더해줌
    if (h1 == 0 or h1 == 12) and m1 == 0 and s1 == 0:
        answer += 1

    return answer

