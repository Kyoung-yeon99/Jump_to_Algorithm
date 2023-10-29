import sys

n, m = map(int, sys.stdin.readline().split())

numList = [i for i in range(1, n+1)] # 1부터 n까지의 자연수

def makeSequence(numList, count, len, sequence):
    if count == len: # m개를 골랐을 경우 수열 출력
        print(sequence)
    else:
        for num in numList:
            newList = numList.copy()
            newList.remove(num)
            if newList: # num 외의 숫자 중에서 하나를 더한 수열 생성
                makeSequence(newList, count+1, len, sequence + str(num) + " ")
            else:
                print(sequence + str(num) + " ") # n과 m이 같을 경우 
    
makeSequence(numList, 0, m, "")