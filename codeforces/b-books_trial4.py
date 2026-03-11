n, t = map(int, input().split())
a = list(map(int, input().split()))
ans = acc = l = 0

for r in range(n):
    acc += a[r]

    while acc > t and l < r:
        acc -= a[l]
        l += 1

    if acc <= t:
        ans = max(ans, r - l + 1)
        
print(ans)