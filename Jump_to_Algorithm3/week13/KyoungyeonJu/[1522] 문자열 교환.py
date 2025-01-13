# a를 모두 연속으로 만들기 위해 필요한 최소 교환 횟수
string = input()
l = len(string)
a_num = string.count('a')
s = list(string[:a_num])

answer = 1000
for i in range(l):
    b_cnt = s.count('b')
    answer = min(answer, b_cnt)
    if answer == 0:
        break
    s.pop(0)
    next = (i+a_num) % l
    s.append(string[next])

print(answer)
