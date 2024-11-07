N = int(input())
channels = []
cur_id = 0
#스페셜 저지란? - 한 개 테케에 정답이 여러개 -> 1,4번만 가지고 풀기
#KBS1 -인덱스 찾아서 첫 번째로 이동 후 리스트 업데이트
#화살표 내려가서 KBS1 찾기 -> 첫 번째로 올리기
#KBS2 -인덱스 찾아서 두 번째로 이동 후 리스트 업데이트
for _ in range(N):
    channels.append(input())
kbs1_id = channels.index('KBS1')
answer = kbs1_id * '1' + kbs1_id * '4'

channels.remove('KBS1')
channels.insert(0,'KBS1')

kbs2_id = channels.index('KBS2')
answer+= kbs2_id * '1' + (kbs2_id - 1) * '4'
print(answer)
