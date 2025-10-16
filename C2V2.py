def f(n: int, m: int, a: [], b: int):
    a[0]=min(a[0], b-a[0])
    for i in range (1, len(a)):
        if max(a[i], b-a[i]) < a[i-1]:
            return "NO"
        if min(a[i], b-a[i]) >= a[i-1]:
            a[i]=min(a[i],b-a[i])
        else:
            a[i]=max(a[i],b-a[i])
    return "YES"
t=int(input())
for _ in range (t):
    n,m=list(map(int, input().split()))
    a=list(map(int,input().split()))
    b=int(input())
    print(f(n,1,a,b))