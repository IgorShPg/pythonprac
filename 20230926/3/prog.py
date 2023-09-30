m=[]
m.append(list(eval(input())))
k=len(m[0])
for i in range(k-1):
    m.append(list(eval(input())))
a=[]
for i in range(k):
    a.append(list(eval(input())))

multi=[]
for i in range(k):
    new=[]
    for j in range(k):
        el=0
        for d in range(k):
            el+=m[i][d]*a[d][j]
        new.append(el)
    multi.append(new)
         
for i in multi:
        print(*i,sep=',')

