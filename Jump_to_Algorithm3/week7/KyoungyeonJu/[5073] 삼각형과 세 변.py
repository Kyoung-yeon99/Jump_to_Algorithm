while True:
    triangles = list(map(int, input().split()))
    if set(triangles) == {0}:
        exit(0)
    l = len(set(triangles))
    m, sum_triangles = max(triangles), sum(triangles)
    if m >= sum_triangles - m:
        print("Invalid")
    elif l == 1:
        print("Equilateral")
    elif l == 2:
        print("Isosceles")
    else:
        print("Scalene")
