def solution(price, money, count):
    fee = 0
    for i in range(count):
        fee += price * (i + 1)

    return abs(money - fee) if money - fee < 0 else 0

'''
# sol2)
return abs(min(money - sum([price*i for i in range(1,count+1)]),0))
'''