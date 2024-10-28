from itertools import permutations, combinations
def solution(k, dungeons):
    p = permutations(dungeons, len(dungeons))
    answer = 0
    for orders in p:
        cnt = 0
        cur_k = k
        for min_st, use_st in orders:
            if cur_k >=min_st:
                cur_k-=use_st
                cnt+=1
        answer = max(answer, cnt)
    return answer
