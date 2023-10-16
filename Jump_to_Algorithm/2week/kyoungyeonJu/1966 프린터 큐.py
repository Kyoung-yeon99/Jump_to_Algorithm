n = int(input())  # 테스트 케이스 수

for i in range(n):
    # 문서 개수, 타켓 인덱스
    a, b = map(int, input().split())
    pri = list(map(int, input().split()))  # 우선수위
    count = 0

    while b >= 0:
        if pri[0] == max(pri):
            pri.remove(pri[0])
            b -= 1
            count += 1
        else:
            pri.append(pri[0])
            pri.remove(pri[0])
            if b == 0:
                b = len(pri) - 1
            else:
                b -= 1

    print(count)




