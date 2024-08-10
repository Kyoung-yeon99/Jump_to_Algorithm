from collections import Counter
def solution(topping):
    ans = 0
    one = Counter(topping)
    two = set()
    
    for t in topping:
        one[t] -= 1
        two.add(t)
        
        if one[t] == 0:
            one.pop(t)
        
        if len(one) == len(two):
            ans += 1
        
    return ans
