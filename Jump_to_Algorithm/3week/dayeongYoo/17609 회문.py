from sys import stdin

input = stdin.readline

num = int(input())
for _ in range(num):
    st = input().strip()
    front, back = 0, len(st) - 1  # 앞, 뒤를 가리키는 포인터
    check = 0

    for _ in range(len(st)):
        if front >= back:
            break
        if st[front] == st[back]:
            front += 1
            back -= 1
            continue

        # 뒷 문자 제거했는데 같을 때, 나머지로 회문 되는지 확인
        if st[front] == st[back - 1]:
            temp = st[front:back]
            if temp[:] == temp[::-1]:
                check = 1
                break
        # 앞 문자 제거했는데 같으면
        if st[front + 1] == st[back]:
            temp = st[front + 1:back + 1]
            if temp[:] == temp[::-1]:
                check = 1
                break

        check = 2
        break

    print(check)
