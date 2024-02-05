n = int(input())

# sol_1 - 등차수열 공식 사용 n(n+1)/2 = s
# for i in range(1, n + 1):
for i in range(4294967295):
    if i * (i + 1) / 2 > n:
        print(i - 1)
        break

# sol_2 - 하나씩 더해보기
ret = 0 # 총 합 저장
cnt = 0 # 더해줄 값 저장
# for i in range(n + 1):
for i in range(4294967295):
    if ret <= n: # 더한 값이 n 보다 작으면 더 더해야 함
        cnt += 1 # 더할 수 += 1
        ret += cnt # 이전 값에 새로운 값 더하기
    else: # 더한 값이 n 보다 크거나 같으면 (탈출 조건)
        print(cnt - 1) # 1씩 증가했으니 -1 해서 출력
        break

'''
for i in range(1, n + 1):
    cnt += 1
    ret += cnt
    if ret > s:
        print(cnt - 1)
        break
        
'''

# 반례
# n = 1 -> 1 , 2 -> 1, 6 -> 3