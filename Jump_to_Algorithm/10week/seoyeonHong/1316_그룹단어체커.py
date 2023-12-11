import sys

count = 0 # 그룹 단어 개수
n = int(sys.stdin.readline()) # 입력 단어 개수

for _ in range(n):
    word = sys.stdin.readline()
    groupword = word[0]
    isGroupWord = True

    for i in range(1, len(word) - 1): 
        if word[i] != word[i-1]: # 이전 문자와 비교
            if word[i] in groupword: # 같은 문자가 연속해서 나타나지 않을 경우
                isGroupWord = False
                break
            groupword += word[i] # 그룹 단어

    if isGroupWord: count += 1 # 그룹 단어일 경우 count 증가
print(count)