t = int(input())
for _ in range(t):
    y0 = set()
    y1 = set()
    n = int(input())
    for _ in range(n):
        a = tuple(map(int, input().split()))
        if a[1] == 1:
            y1.add(a[0])
        else:
            y0.add(a[0])
    m = y0 & y1
    c = (n-2)*len(m)
    y0x = list(y0)
    y1x = list(y1)
    ly0 = len(y0)
    ly1 = len(y1)
    for x in range(ly0-1):
        for i in (1, 2):
            if x+i < ly0   and  y0x[x+i]-y0x[x] == 2 and (y0x[x]+1 in y1):
                c+=1
    for x in range(ly1-1):
        for i in (1, 2):
            if x+i < ly1   and  y1x[x+i]-y1x[x] == 2 and (y1x[x]+1 in y0):
                c+=1
    print(c)


        









