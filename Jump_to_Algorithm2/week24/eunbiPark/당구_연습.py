def solution(m, n, sx, sy, balls):
    ans = []
    for i in range(len(balls)):
        ex, ey = balls[i][0], balls[i][1]
        distance = float('inf')
        temp = []
        
        if sx!=ex or sy > ey: 
            temp.append(abs(sx-ex)**2 + abs(2*n-sy-ey)**2)  #우
        if sx!=ex or sy < ey: 
            temp.append(abs(sx-ex)**2 + abs(sy+ey)**2)      #좌
        if sy!=ey or sx < ex: 
            temp.append(abs(sx+ex)**2 + abs(sy-ey)**2)      #상
        if sy!=ey or sx > ex: 
            temp.append(abs(2*m-sx-ex)**2 + abs(sy-ey)**2)  #하
        
        for dist in temp:
            if dist < distance:
                distance = dist
        
        ans.append(distance)
    return ans
