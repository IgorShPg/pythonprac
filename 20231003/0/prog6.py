def adders(n):
    res=[]
    for i in range(n):
        def adder(x,j=i):
            return x+j
        res.append(adder)
    return res

