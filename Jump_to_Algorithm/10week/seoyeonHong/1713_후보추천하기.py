# 오류...
n = int(input())
m = int(input())
rec = list(map(int, input().split()))
rec_cnt = [0 for _ in range(m+1)]
frame = []
min_num = 0
min_cnt = m

for r in rec:
    print('frame', frame)
    rec_cnt[r] += 1 # 추천수 +1
    if len(frame) < n and r not in frame: # 비어있는 경우 사진틀에 게시
        frame.append(r)
    elif r not in frame: # 새로운 학생 사진 게시
        print('remove', min_num)
        frame.remove(min_num) # 가장 추천수가 적고 오래된 사진 삭제
        frame.append(r) # 새로운 사진 게시
    print('post', r)
    frame_cnt = []
    for num in frame:
        frame_cnt.append(rec_cnt[num])
    min_cnt = min(frame_cnt) # 현재 게시된 학생 중 가장 적은 추천수
    print('min_cnt', min_cnt)
    for num in frame:
        if rec_cnt[num] == min_cnt: # 가장 적은 추천수를 가지고 오래된 사진
            min_num = num
            print('min_num', min_num)
            break

frame.sort() # 오름차순 정렬
for f in frame:
    print(f, end=' ')
