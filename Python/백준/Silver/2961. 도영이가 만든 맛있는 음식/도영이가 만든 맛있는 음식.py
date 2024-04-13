def dfs(depth, start):
    global result
    if depth == len_:
        sour = 1
        bitter = 0
        for i in arr:
            sour *= i[0] 
            bitter += i[1] 
        if abs(bitter - sour) < result: 
            result = abs(bitter - sour)
        return 
   
    for i in range(start, N):
        arr.append(cuisine[i])
        dfs(depth + 1, i + 1)
        arr.pop()


N = int(input())
cuisine = [list(map(int, input().split())) for i in range(N)]
arr = []
result = 1 << 100  

for i in range(1, N + 1):  
    len_ = i
    dfs(0, 0)

print(result)