# 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램
N, S = map(int, input().split()) 
seq = list(map(int, input().split())) # 수열
count = N # 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이
start, end, part_sum = 0, 0, seq[0]
if sum(seq) < S: # 수열의 총합이 S보다 작을 경우
    print(0)
else:
    while start <= end < N:
        if part_sum < S and end < N-1: # 부분수열의 합이 S보다 작고 end가 N-1보다 작을 경우
            end += 1 # end +1 
            part_sum += seq[end]
        elif part_sum >= S: # 부분수열의 합이 S 이상일 경우
            count = min(count, end - start + 1) # count 갱신
            part_sum -= seq[start]
            start += 1 # start +1
        else: # end == N-1 일 경우
            part_sum -= seq[start]
            start += 1
            if part_sum >= S:
                count = min(count, end - start + 1)
    print(count)
