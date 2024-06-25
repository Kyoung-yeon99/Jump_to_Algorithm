# https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    for word in goal: # 각 단어에 대해
        if cards1 != [] and cards1[0] == word: # cards1에 해당 단어가 있다면
            cards1.remove(word)
        elif cards2 != [] and cards2[0] == word: # cards2에 해당 단어가 있다면
            cards2.remove(word)
        else: # 순서대로 카드를 사용하여 단어 배열을 만들 수 없다면
            return "No"
    return "Yes"