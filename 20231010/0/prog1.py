import decimal

def esum(N,one):
    k=1
    sum=1
    for i in range(1,N+1):
        k=k*i
        z=1/k
        sum+=z
    return type(one)(sum)

print(esum(100,decimal.Decimal(1)))
