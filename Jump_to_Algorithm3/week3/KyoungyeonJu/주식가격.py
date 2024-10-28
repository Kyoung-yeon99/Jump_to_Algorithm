def solution(prices):
    answer = []
    m = prices[0]
    for i in range(len(prices)-1):
        t = 0
        for j in range(i+1, len(prices)):
            if prices[j] < prices[i]:
                t += 1
                break
            t += 1
        answer.append(t)

    answer.append(0)
    return answer