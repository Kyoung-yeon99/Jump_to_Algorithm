from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0 
        
        for need, minus in p:
            if tmp >= need:
                tmp -= minus
                cnt += 1
        answer = max (cnt, answer)
    return answer 
