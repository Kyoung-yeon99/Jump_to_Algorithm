import sys

n, m = map(int, sys.stdin.readline().split())

numList = [i for i in range(1, n+1)] # 1부터 n까지의 자연수
numSets = []

def combination(numList, sequence, count, len):
    if count == len:
        numSet = set(map(int, sequence.split())) # set 자료구조로 변환
        if numSet not in numSets: # 출력하지 않은 조합일 경우 출력
            numSets.append(numSet)
            print(sequence)
    else:
        for num in numList:
            newList = numList.copy()
            newList.remove(num)
            combination(newList, sequence + str(num) + " ", count + 1, len)

if m == 1:
    for i in range(1, n+1):
        print(i)
elif n == m:
    for i in range(1, n+1):
        print(i, end=' ')
else:
    combination(numList, "", 0, m)