def solution(word):
    dict = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    diff = [781, 156, 31, 6, 1]
    answer = 0

    for i in range(len(word)):
        c = word[i]
        answer += (1 + diff[i]*dict[c])
        print(c, diff[i]*dict[c], answer)

    return answer


"""
# 백트래킹(DFS)
def solution(word):
    alphabets = ['A','E','I','O','U']
    global answer
    answer = 0

    def dfs(string):
        global answer
        answer += 1
        print("dfs ", string, answer)

        if string == word:
            return True

        if len(string) == 5:
            return False

        for alpha in alphabets:
            if dfs(string + alpha) == True:
                print("in in ", string+alpha)
                return True

    for alpha in alphabets:
        print("밖", alpha)
        if dfs(alpha) == True:
            print("밖 true answer=", answer)
            return answer
"""