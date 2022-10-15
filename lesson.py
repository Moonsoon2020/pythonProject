for _ in range(int(input())):
    n = int(input())
    d = list(map(int, input().split()))
    a = [d[0]]
    for i in range(1, n):
        k = a[-1]
        b = d[i]
        if (b - k <= 0 and b + k >= 0) or (b - k >= 0 and b + k <= 0):
            print(b, k)
