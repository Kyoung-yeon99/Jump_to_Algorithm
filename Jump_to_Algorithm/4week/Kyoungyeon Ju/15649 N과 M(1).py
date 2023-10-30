def backTracking():
    if len(result) == m:
        print("len(result) == m일 때", result)
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        print("i=",i)
        if i not in result:
            result.append(i)
            print("result.append(i)","i는", i, result)
            backTracking()
            result.pop()
            print("result.pop()","i는", i, result)
        else:
            print(i,"는 결과 리스트에 존재", result)


n, m = map(int, input().split())
result = []
backTracking()


"""
from itertools import permutations
n, m = map(int, input().split())
p = permutations(range(1, n+1), m)
for i in p:
    print(" ".join(map(str,i))
"""