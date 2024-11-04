# 파일명에 포함된 숫자를 반영한 정렬 기능
def solution(files):
    answer = []

    for f in files:
        head, number = '', 0
        for i in range(len(f)):
            if str.isdigit(f[i]):
                head = f[:i]
                for j in range(i+1, len(f)):
                    if not str.isdigit(f[j]):
                        number = int(f[i:j])
                        break
                break
        print(head, number)

    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))