# https://school.programmers.co.kr/learn/courses/30/lessons/87946

# 유저가 탐험할수 있는 최대 던전 수
def solution(k, dungeons):
    global answer
    answer = 0
    N = len(dungeons) # 던전의 개수
    
    def explore(hp, depth, visited): # 피로도, 탐험한 던전의 수, 던전 탐험 여부
        global answer 
        
        if hp == 0 or depth == N: # 피로도가 모두 소모됐거나 모든 던전을 탐험했을 경우
            answer = max(answer, depth) # 탐험 종료
            return
            
        exploreable = False 
        
        for i in range(N):
            
            need, consume = dungeons[i]
            
            if not visited[i] and need <= hp: # 아직 탐험하지 않은 i번째 던전을 탐험할 수 있다면
                visited[i] = True
                explore(hp - consume, depth + 1, visited)
                visited[i] = False
                exploreable = True
            
        if not exploreable: # 다른 던전을 더 탐험할 수 없다면
            answer = max(answer, depth) # 탐험 종료
            return
            
            
    for i in range(N): # 첫번째로 탐험할 던전 설정
        
        need, consume = dungeons[i]
        
        if need <= k: # i번째 던전을 탐험할 수 있다면
            visited = {i: False for i in range(N)}
            visited[i] = True
            explore(k - consume, 1, visited)
            
        if answer == N: # 모든 던전을 탐험 가능하다면 탐색 종료
            return answer
    
    return answer
