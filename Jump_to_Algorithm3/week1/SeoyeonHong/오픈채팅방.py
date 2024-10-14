# https://school.programmers.co.kr/learn/courses/30/lessons/42888

# 최종적으로 방을 개설한 사람이 보게 되는 메시지
def solution(record):
    message = []
    last_nickname = {}
    for r in record:
        words = r.split(' ')
        if len(words) == 2: # 채팅방을 나갔을 경우
            message.append([words[1], "님이 나갔습니다."])
        else: # 채팅방을 들어오거나 닉네임을 변경했을 경우
            action, uid, nickname = words
            if action == "Enter": # 채팅방을 들어왔을 경우
                message.append([uid, "님이 들어왔습니다."])
            last_nickname[uid] = nickname # 닉네임 갱신
            
    for i in range(len(message)):
        u, s = message[i]
        message[i] = last_nickname[u] + s # 최종 닉네임이 포함된 문구로 변경
            
    return message