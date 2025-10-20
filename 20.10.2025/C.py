t = int(input())
for _ in range(t):
    x, y, s = map(int, input().split())
    mx = (x+s-1)//s
    my = (y+s-1)//s
    if mx>my:
        print(mx*2-1)
    else:
        print(my*2)