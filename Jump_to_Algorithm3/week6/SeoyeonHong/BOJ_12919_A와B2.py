from collections import deque

S = input()
T = input()
answer = 0
q =  deque([T])

if S not in T and S[::-1] not in T: # S에 문자를 추가하거나 뒤집어서 만들 수 없다면
    print(answer)
else:
    while q:
        t = q.popleft()
        if t == S: # S와 일치하는 문자열일 경우
            answer = 1
            break
        if len(t) < len(S): # S보다 길이가 짧을 경우
            break

        if len(t) > 1:
            if t[-1] == 'A': # 마지막 문자가 A라면 제거
                q.append(t[:-1])
            if t[0] == 'B': # 첫번째 문자가 B라면 나머지 문자열 뒤집기
                q.append(t[:0:-1])

print(answer)
