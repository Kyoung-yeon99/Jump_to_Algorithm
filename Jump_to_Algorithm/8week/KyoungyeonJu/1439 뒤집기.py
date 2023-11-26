s = input()

cnt_0 = 0
cnt_1 = 0

if s[0] == '0':
    cnt_0 += 1
else:
    cnt_1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i] != '0':  # 1 옆에 0
            cnt_0 += 1
        else:  # 0 옆에 1
            cnt_1 += 1

print(min(cnt_0, cnt_1))

"""
 ~~ 신기한 풀이 ~~
n = input()
print(len(set(list(n))))

arr1 = n.split('0')
arr2 = n.split('1')
print(arr1, len(arr1), arr1.count(''))
print(arr2, len(arr2), arr2.count(''))

a = len(arr1) - arr1.count('')
b = len(arr2) - arr2.count('')

print(min(a, b))
"""


