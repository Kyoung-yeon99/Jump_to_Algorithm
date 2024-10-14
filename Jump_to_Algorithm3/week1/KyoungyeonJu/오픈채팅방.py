def solution(record):
    answer, real_answer, ids = [], [], []
    d = {}

    for r in record:
        words = r.split()
        if words[0] == "Enter":
            d[words[1]] = words[2]
            ids.append(words[1])
            answer.append("님이 들어왔습니다.")
        elif words[0] == "Leave":
            ids.append(words[1])
            answer.append("님이 나갔습니다.")
        elif words[0] == "Change":
            d[words[1]] = words[2]

    for i, word in zip(ids, answer):
        real_answer.append(f"{d[i]}{word}")

    return real_answer