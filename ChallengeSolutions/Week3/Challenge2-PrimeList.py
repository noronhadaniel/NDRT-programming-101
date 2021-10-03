def primelist(N):
    if N <= 1:
        return []
    elif N == 3:
        return [2]
    primelist = []

    for x in range(2,N):
        for i in range(2,x):
            if x%i == 0:
                break
            elif (x%i != 0) & (i == x-1):
                primelist.append(x)

    return primelist
    
print(primelist(6))
