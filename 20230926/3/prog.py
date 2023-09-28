k=0
m=[]
while s:=input():
    m.append(eval(s))
    k+=1
a=[]
b=[]
z=k//2
for i in range(0,z):
    a.append(m[i])
for i in range(z,k):
    b.append(m[i])
multi=[[0 for i in range(z)]for j in range(z)]
for i in range(z):
    for j in range(z):
        for d in range(z):
            multi[i][j]+=a[i][d]*b[d][j]

for i in multi:
        print(*i,sep=',')

