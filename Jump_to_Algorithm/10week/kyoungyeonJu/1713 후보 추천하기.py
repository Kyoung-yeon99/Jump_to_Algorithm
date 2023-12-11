n = int(input())  # 사진틀 개수
m = int(input())  # 총 추천 횟수
nums = list(map(int, input().split()))  # 추천 번호
pics = dict()
pics_key = []

for num in nums:
    if num in pics: # 이미 게시된 학생 사진
        pics[num] += 1
    else:  # 아직 게시되지 않은 학생
        if len(pics) >= n:  # 남은 사진 틀이 없다면
            # 추천 횟수가 가장 적은 학생번호 찾기
            remove = []
            for k, v in pics.items():
                if v == min(pics.values()):
                    remove.append(k)
            # pics_key에서 먼저 나오는 거 찾기
            for key in pics_key:  # pics_key는 리스트이기 때문에 순서가 있다
                if key in remove:
                    pics.pop(key)
                    pics_key.remove(key)
                    break
        pics[num] = 1
        pics_key.append(num)

pics_key.sort()
print(*pics_key)




