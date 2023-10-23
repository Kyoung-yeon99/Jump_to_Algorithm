n = int(input())
a = list(input() for _ in range(n))
count = 0
flag = False

for i in range(n):  # 단어 개수만큼
    str_ = a[i]
    if len(a[i]) == 1:
        flag = True
    for j in range(len(a[i])-1):  # 단어 길이만큼
        last = str_[j]
        new = str_[j+1]
        if last == new:  # last와 new가 동일하면
            flag = True
        else:  # last와 new가 다르면
            new_str = str_[:j+1]
            if new_str.find(new) == -1:  # 전에 들어온 문자와 같은 문자가 아니라면
                flag = True
            else:  # 연속하지 않고 떨어진 단어가 있다면
                flag = False
                break
    if flag:
        count += 1

print(count)

"""
# set() 이용
n = int(input())
count = 0

for i in range(n):
    a = list(input())
    b = 1
    for j in range(len(a)-1):
        if a[j] != a[j+1]:
            b += 1
    if b == len(set(a)):
        count += 1

print(count)
"""



