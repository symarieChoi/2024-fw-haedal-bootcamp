n = int(input())
k = int(input())

start, end = 1, n**2
result = 0

if n**2 == k:
    print(k)
else:
    while(start < end):
        mid = (start+end)//2

        c = 0
        for i in range(1,n+1):
            c += min(mid // i, n)
        
        if c >= k:
            end = mid
            result = mid
        elif c < k:
            start = mid+1
    print(result)