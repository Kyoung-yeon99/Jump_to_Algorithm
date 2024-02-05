s = int(input())
# 개수 세기
total = 0
cnt = 0

for i in range(1, s + 1):
    cnt += 1
    total += i

    if total > s:  # total==s이 아닌 이유는 s를 초과하는 경우를 감지하고 그때까지의 개수를 출력하기 위함임.
        break

# 예외 처리
if s == 1:
    print(1)
else:
    print(cnt - 1)  # s 초과하는 경우이므로, -1 해줌.
