word = list(input())
remove = list(input())

stack = []
i = 0

while i < len(word): #문자 한바퀴 돌면서 폭발 탐색
    #문차 추가하면서 맨 뒤애들이랑 제거할 문자 비교
    stack.append(word[i])
    if stack[-len(remove):] == remove:#폭발
        for _ in range(len(remove)):#지울 문자열 개수만큼 pop
            stack.pop()
    i+=1

word = ''.join(list(stack))


if word:
    print(word)
else:
    print("FRULA")

