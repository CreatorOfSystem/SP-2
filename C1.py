h = int(input())
for _ in range(h):
    ch, mn = map(int, input().split())
    n = list(map(int, input().split()))
    m = int(input())
    # for 0 index
    if ch == 1: print("Yes")
    else:
        new = m-n[0]

        n[0] = min(new, n[0])

        for i in range(1,ch):
            new = m - n[i]
            amin = min(new, n[i])
            amax = max(new, n[i])
            if n[i-1]<=amin:
                n[i] = amin
            elif n[i-1]<=amax:
                n[i] = amax
            else:
                print("NO")
                break
        else:
            print("YES")

        


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

