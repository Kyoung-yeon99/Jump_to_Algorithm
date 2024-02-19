X = int(input()) # 원하는 막대의 길이
sum = 64 # 가지고 있는 막대의 합
bar = [64] # 가지고 있는 막대 길이 리스트

while True: # 가지고 있는 막대의 합이 X가 될 때 까지
    if sum > X: # 막대의 합이 X보다 크다면
        sb = bar.pop() # 가장 짧은 막대를 절반으로 자른다
        sb = sb // 2
        bar.append(sb)
        if sum - sb >= X: # 막대의 합이 X 이상일 경우 자른 막대의 절반을 버린다
            sum -= sb
        else:
            bar.append(sb)
    else:
        break

print(len(bar)) # 막대기의 개수 출력