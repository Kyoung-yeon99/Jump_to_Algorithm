from collections import defaultdict

def solution(edges):
    answer = [0, 0, 0, 0]
    start, donut, bar, eight = 0, 1, 2, 3
    d = defaultdict(list)

    # 진출 차수 0: 바 그래프의 리프 노드
    # 진출 차수 1: 의미 없음
    # 진출 차수 2: 8자 그래프의 중앙 노드 혹은 루트 노드
    # 진출 차수 2개 초과: 루트 노드
    out_in = defaultdict(lambda: [0, 0])

    for s, e in edges:
        d[s].append(e)
    print(d)

    for node, nodes in d.items():
        for n in nodes:
            out_in[node][0] += 1
            out_in[n][1] += 1
    print(out_in)

    for node, degrees in out_in.items():
        outd, ind = degrees
        print(f'node = {node} outd = {outd} ind = {ind}')

        if outd == 0:
            answer[bar] += 1
            print(f'outd==0 node = {node} {answer}')
        elif outd == 2:
            if ind > 0:
                answer[eight] += 1
                print(f'outd==2 node = {node} ind = {ind} {answer}')
            else:
                answer[start] = node
                root = node
        elif outd > 2:
            answer[start] = node
            root = node
            #print(f'outd>2 node = {node} {answer} {root}')

    answer[donut] = out_in[root][0] - answer[bar] - answer[eight]
    print(answer)
    return answer


tcs = [
    [[2, 3], [4, 3], [1, 1], [2, 1]],
    [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
    ]

solution(tcs[1])