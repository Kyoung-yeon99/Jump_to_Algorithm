def solution(sequence, k):
        n = len(sequence)
        start, end, sum = 0, 0, sequence[0]
        ans = [0, float('inf')]
        
        while start <= end and end < n:
            # 1. 현재 수열의 합 < k
            # end += 1
            if sum < k and end < n-1: # end += 1 할 것이기에 범위 체크
                end += 1
                sum += sequence[end]
            
            # 2. 현재 수열의 합 > k
            # start += 1
            elif sum > k:
                sum -= sequence[start]
                start += 1
                
            # 3. 현재 수열의 합 == k
            elif sum == k:
                # 기존에 등록된 수열의 길이와 비교 
                # 같으면 인덱스 작은 것을 등록해야 하기에 갱신하지 않는다
                if ans[1] - ans[0] > end - start: 
                    ans = [start, end]
                
                # sum = k를 만족하는 더 짧은 수열이 있을 수 있기에 start += 1 
                sum -= sequence[start]
                start += 1
            
            # 4. (1, 2, 3) 조건을 만족하지 못했는데 end를 갱신하지 못해 무한루프인 경우 방지
            else:
                if end == n-1:
                    break
                
        return ans

# def solution(sequence, k):
#     n = len(sequence)

#     max_sum = 0
#     end = 0
#     interval = n

#     for start in range(n):
#         while max_sum < k and end < n:
#             max_sum += sequence[end]
#             end += 1
#         if max_sum == k and end-1-start < interval:
#             res = [start, end-1]
#             interval = end-1-start
#         max_sum -= sequence[start]

#     return res
