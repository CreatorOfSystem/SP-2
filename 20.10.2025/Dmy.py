t = int(input())
for _ in range(t):
    data = []
    y0 = set()
    y1 = set()
    n = int(input())
    for _ in range(n):
        a = tuple(map(int, input().split()))
        data.append(a)
        if a[1] == 1:
            y1.add(a[0])
        else:
            y0.add(a[0])
    m = y0 & y1
    c = (n-2)*len(m)
    y0x = list(y0)
    y1x = list(y1)
    for x in range(len(y0)-1):
        for x2 in range(x+1, len(y0)):
            if x2-x == 2 and (x+1 in y1):
                c+=1
    for x in range(len(y1)-1):
        for x2 in range(x+1, len(y1)):
            if x2-x == 2 and (x+1 in y0):
                c+=1
    print(c)


        









