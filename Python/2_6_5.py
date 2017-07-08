n = int(input())

step = 0
a = [[0] * n for i in range(n)] 
k = 1

while k <= n * n:
    # right
    for i in range(step, n - step - 1):
        if k > n * n:
            break
        a[step][i] = k
        k += 1
    # down
    for i in range(step, n - step - 1):
        if k > n * n:
            break
        a[i][n - step - 1] = k
        k += 1
    # left
    for i in range(n - step - 1, step, -1):
        if k > n * n:
            break
        a[n - step - 1][i] = k
        k += 1
    # top
    if n - step -1 == step:
        a[step][step] = k
        k += 1
    else:
        for i in range(n - step - 1, step, -1):
            if k > n * n:
                break
            a[i][step] = k
            k += 1
    step += 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print() 
