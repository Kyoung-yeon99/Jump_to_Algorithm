def solution(n, k):
    word = ''
    while n:
        word = str(n%k) + word
        n //= k
    
    word = word.split('0')
    
    cnt = 0
    for w in word:
        if len(w) == 0:
            continue
        if int(w) < 2:
            continue
        flag = True # 소수 o -> True
        # 소수 찾기 
        for i in range(2, int(int(w) ** 0.5) + 1): 
            if int(w) % i == 0:
                flag = False 
                break 
        if flag:
            cnt += 1
    
    return cnt
