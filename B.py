h = int(input())
for _ in range(h):
    m = input()
    for i in range(len(m)-1):
        if m[i]==m[i+1]:
            print("1")
            break
    else:
        print(len(m))