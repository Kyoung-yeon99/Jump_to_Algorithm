from itertools import combinations
#전체 경우의 수 다 곱하기 - 모두 옷 안입은 경우의수(1) 빼기
def solution(clothes):
    cloth_dic = {}
    for name , cloth in clothes:
        if cloth_dic.get(cloth) == None: #딕셔너리에 없으면
            cloth_dic[cloth] = 2
        else: #있으면 리스트 추가
            cloth_dic[cloth] +=1
    print(cloth_dic)
    answer = 1 # 팩토리얼 곱하기
    for cnt in cloth_dic.values():
        answer*=cnt
    return answer -1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
