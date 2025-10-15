h = int(input())
for _ in range(h):
    ch, mn = map(int, input().split())
    n = list(map(int, input().split()))
    m = list(map(int, input().split()))
    mm = max(m)
    mim = min(m)
    # for 0 index
    if ch == 1: print("Yes")
    else:
        
        newmi = mim - n[0]
        n[0] = min(newmi, n[0])

        for i in range(1,ch):
            newmi = mim - n[i]
            newm = mm - n[i]
            amin = min(newmi, n[i])
            amax = max(newm, n[i])
            if n[i-1]<=amin:
                n[i] = amin
            elif n[i-1]<=amax:
                n[i] = amax
            elif n[i-1]<n[i]: continue
            else:
                print("NO")
                break
        else:
            print("YES")

        
