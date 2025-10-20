t = int(input())
for _ in range(t):
    n = int(input())
    data = []
    x_count = {}
    for _ in range(n):
        x, y = tuple(map(int, input().split()))
        data.append((x,y))
        x_count[x] = x_count.get(x, 0) +1
    m = len(list(filter(lambda key: x_count[key] == 2, x_count)))
    result = (n-2)*m


t 