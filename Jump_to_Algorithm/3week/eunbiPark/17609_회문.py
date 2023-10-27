import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    word = input().rstrip()
    front, back = 0, len(word) - 1
    check = 0

    for _ in range(len(word)):
        if front >= back:
            break
        if word[front] == word[back]:
            front += 1
            back -=1
            continue

        # 뒷문자 제거
        if word[front] == word[back -1]:
            temp = word[front:back]
            if temp[:] == temp[::-1]:
                check = 1
                break

        # 앞문자 제거
        if word[front + 1] == word[back]:
            temp = word[front + 1 : back + 1]
            if temp[:] == temp[::-1]:
                check = 1
                break

        check = 2
        break

    print(check)