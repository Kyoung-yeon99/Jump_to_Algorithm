S = list(map(int, input()))
num = 1
std = S[0]  # 기준은 첫번째 문자

for i in S[1:]:
    if std == i:  # 같으면 패스
        continue
    else:  # 같지 않으면 num + 1
        std = i
        num += 1

print(num//2)

"""
num default는 1 
연속된 숫자들의 부분 개수 | 출력 
3 1
1 0
2 1
9 4
5 2
"""