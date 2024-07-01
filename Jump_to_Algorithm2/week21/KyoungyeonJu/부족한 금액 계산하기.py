def solution(price, money, count):
    total_price = price * (count * (count + 1) // 2)

    if money >= total_price:
        return 0
    else:
        return total_price - money

    # price *(1+2+...+n)
    # n % 2 == 0 n*n+1/2
    # n % 2 == 1 n*n+1/2
