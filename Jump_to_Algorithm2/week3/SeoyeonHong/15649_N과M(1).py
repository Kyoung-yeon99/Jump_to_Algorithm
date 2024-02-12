# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열, 수열은 사전 순으로 증가 (1 ≤ M ≤ N ≤ 8)
n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

def printSequence(seq, left, depth):
    if depth == 0:
        print(seq)
    else:
        for l in left:
            newLeft = left.copy()
            newLeft.remove(l)
            if seq == "":
                printSequence(str(l), newLeft, depth-1)
            else:
                printSequence(seq + " " + str(l), newLeft, depth-1)

printSequence("", nums, m)

# 순열 라이브러리 사용
# from itertools import permutations
# n, m = map(int, input().split())
# for s in permutations([i for i in range(1, n+1)], m):
#     print(*s)

# 백트래킹 사용
# N, M = map(int, input().split())
# ans = []

# def back():
#     if len(ans) == M: # 배열의 길이를 확인(재귀함수를 마치는 조건)
#         print(*ans)
#         return 

#     for i in range(1, N+1): # 1 ~ N 까지
#         if i not in ans: # 중복 확인(백트래킹에서의 한정 조건)
#             ans.append(i) # 배열 추가
#             back() # 백트래킹
#             ans.pop() # 전 단계로 이동
#     return
        
# back()
