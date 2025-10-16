t=int(input())
for _ in range(t):
    n = int(input())
    p = []
    for d in range(n):
        p.append("0")
    # p = [int(o)=0 for o in range(h)]
         
    for i in range(n, 0, -1):
        s = input()
        x = s.find("#")
        p[i-1] = x+1
    a = ""
    for w in range(n):
        a = a+" "+ str(p[w])
    # c = 0
    # for x1 in c:
    #     a = ''.join(p)
    print(a)
             