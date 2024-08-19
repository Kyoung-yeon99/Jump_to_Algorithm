def solution(cards):
    ans = []
    n = len(cards)
    visited = [0 for _ in range(n + 1)]
    
    for c in cards:
        if not visited[c]:
            temp = []
            while c not in temp:
                temp.append(c)
                c = cards[c-1]
                visited[c] = 1
            ans.append(len(temp))
    
    if ans[0] == n:
        return 0
    else:
        ans.sort(reverse = True)
    
    return ans[0] * ans[1]
