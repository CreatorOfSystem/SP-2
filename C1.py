h = int(input())
for _ in range(h):
    n, m = map(int, input().split())
    ch = list(map(int, input().split()))
    m = int(input())
    # for 0 index
    if n == 1: print("Yes")
    else:
        new = m-n[0]
        amin = min(new, n[0])
        amax = max(new, n[0])
        if amin<=n[i+1] or amin<=m-n[1]:
            n[0]==amin
            for i in range(1,n-1):
                new = m - n[i]
                amin = min(new, n[i])
                amax = max(new, n[i])
                if n[i-1]<=amin and (amin<=n[i+1] or amin<=m-n[i+1]):
                    n[i] = amin
                elif n[i-1]<=amax and (amax<=n[i+1] or amax<=m-n[i+1]):
                    n[i] = amax
                else:
                    print("NO")
                    break
            else:
                print("Yes")

        else:
            print("NO")
        


    # i = 0
    # while i < n - 1:
    #     if ch[i] <= ch[i + 1] or (i == n - 2 and ch[i] <= m - ch[i + 1]):
    #         i += 1
    #     elif (i == 0 and m - ch[i] <= ch[i + 1]) or (ch[i - 1] <= m - ch[i] <= ch[i + 1]):
    #         ch[i] == m - ch[i]
    #         i += 1
    #     else:
    #         print("No")
    #         break
    # else:
    #     print("Yes")

