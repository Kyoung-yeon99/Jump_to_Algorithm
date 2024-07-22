def solution(s):
    a = list(map(int, s.split()))

    answer = "" + str(min(a)) + " " + str(max(a))
    return answer