import math
t=int(input())
for _ in range(t):
    x,y,k=map(int,input().split())
    m = max(x,y)
    mi = min(x,y)
    prm = math.ceil(m/k)
    prmi = prm
    if mi%k !=0:
        prmi += 1
    elif  m%k == 0 :
        prmi = prm-1
    else:
        prmi = prm 
    print(prm+prmi)
