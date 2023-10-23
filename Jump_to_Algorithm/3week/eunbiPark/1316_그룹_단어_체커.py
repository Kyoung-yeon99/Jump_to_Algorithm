# 그룹 단어의 개수를 출력하는 프로그램
n = int(input())
word = []
for _ in range(n): word.append(input())
cnt = n
for w in word:
    for i in range(len(w)-1):
        if w[i] == w[i+1]:
            pass
        elif w[i] in w[i+1:]:
            cnt -= 1
            break

print(cnt)