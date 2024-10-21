# https://school.programmers.co.kr/learn/courses/30/lessons/42860

# 주어진 문자열을 만들기 위해 필요한 조이스틱 조작 횟수의 최솟값
def solution(name):
    nums = [min(ord(a) - 65, 91 - ord(a)) for a in list(name)] # 'A'로 만들기 위해 필요한 버튼 조작 횟수
    n = len(nums) # 문자열 길이
    visit = [i for i in range(n) if nums[i] != 0] # 'A'가 아닌 문자들의 위치(인덱스)

    if visit: # 바꿀 문자가 있다면
        min_move  = min(max(visit), n-min(visit)) # 최소 이동횟수, 직진하는 경우로 초기화

        for i in range(len(visit)-1):
            a, b = visit[i], visit[i+1]
            # a까지 오른쪽으로 갔다가 다시 왼쪽으로 b까지 가는 경우, 
            # b까지 왼쪽으로 갔다가 다시 오른쪽으로 a까지 가는 경우
            min_move = min(min_move, 2 * a + n - b, a + 2 * (n - b)) 
            
        return min_move + sum(nums)
    else: # 바꿀 문자가 없다면
        return 0

# 순열 활용 풀이
# from itertools import permutations

# def solution(name):
#     nums = [min(ord(a) - 65, 91 - ord(a)) for a in list(name)]
#     n = len(nums)
#     check = n - nums.count(0)
#     min_move = n
#     visit = []
#     for i in range(n):
#         if nums[i] != 0:
#             visit.append(i)

#     roots = list(permutations(visit, check))
#     for root in roots:
#         move = min(root[0], n-root[0])
#         for i in range(check-1):
#             diff = abs(root[i]-root[i+1])
#             move += min(diff, n-diff)
#         min_move = min(min_move, move)

#     return min_move + sum(nums)