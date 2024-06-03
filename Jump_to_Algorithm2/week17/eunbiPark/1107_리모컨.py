n = int(input())
m = int(input())

if m:
    nums = tuple(input().split()) # 문자열로 받기
else:
    nums = ()

# +, - 버튼만 눌렀을 때의 경우의 수 - mn의 초깃값 설정
ans = abs(100 - n)
# 브루트포스
for num in range(1000001):
    # 고장난 번호를 문자열로 확인하기 위해 문자열 처리
    for s_num in str(num):
        if s_num in nums: # 고장난 번호
            break

    # 고장난 번호를 누른 게 아니라면
    else:
        # len(str(num): 누른 번호의 개수
        # abs(num - n): 누른 +, - 의 개수
        ans = min(ans, len(str(num)) + abs(num - n))

print(ans)