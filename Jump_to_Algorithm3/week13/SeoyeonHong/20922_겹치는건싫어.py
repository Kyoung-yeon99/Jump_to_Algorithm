# 같은 원소가 K개 이하로 들어 있는 최장 연속 부분 수열의 길이
N, K = map(int, input().split())
seq = list(map(int, input().split())) # 주어진 수열
start, end = 0, 0 # 연속 부분 수열의 시작과 끝
count = [0] * 100001 # 연속 부분 수열의 정수의 개수
max_length = 1 # 최장 연속 부분 수열의 길이
max_count = 1 # 가장 많이 포함된 정수의 개수
count[seq[start]] += 1 # 첫번째 원소를 

while N - start > max_length: # 현재 최장 연속 부분 수열의 길이보다 남은 수열의 길이가 길다면
    if max_count <= K: # 같은 정수가 K개 이하일 경우 수열 길이 +1
        end += 1 # 부분 수열 증가
        if end < N: # 부분 수열의 끝이 인덱스 범위를 벗어나지 않았다면
            count[seq[end]] += 1 # 추가한 정수의 개수 증가
            max_count = max(max_count, count[seq[end]])
            if max_count > K: # 가장 많은 정수의 개수가 K개를 넘었다면
                while max_count > K:
                    if seq[start] == seq[end]:
                        max_count -= 1
                    count[seq[start]] -= 1
                    start += 1 # 앞에서부터 부분 수열에서 제거
            max_length = max(max_length, end-start+1) # 최장 부분 수열의 길이 갱신
        else:
            break
    
print(max_length)

