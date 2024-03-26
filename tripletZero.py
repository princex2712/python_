x = [1, -6, 4, 2, -1, 2, 0, -2, 0]
x.sort()
result = []

for i in range(len(x)-2):
    if i > 0 and x[i] == x[i-1]:
        continue
    l,r = i+1,len(x)-1

    while l < r:
        s = x[l] + x[r] + x[i]
        if s > 0:
            r -= 1
        elif s < 0:
            l += 1
        else:
            result.append((x[i], x[l], x[r]))
            while l < r and x[l] == x[l+1]:
                l += 1
            while l < r and x[r] == x[r-1]:
                r -= 1
            l += 1 
            r -= 1  

print(result)
