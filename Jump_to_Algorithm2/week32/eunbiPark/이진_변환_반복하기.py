def solution(s):
    zero, conver = 0, 0
    
    while s != '1':
        if '0' in s:
            zero += s.count('0')
            s = s.replace('0', '')
        
        length = len(s)
        s = str(format(length, 'b'))
        conver += 1
    
    return [conver, zero]
