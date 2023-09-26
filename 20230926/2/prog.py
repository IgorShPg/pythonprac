a=list(eval(input()))
b=a.copy()
k=0
for i in b:
    z=(i**2)%100
    b[k]=z
    k+=1
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if b[i]>b[j]:
            b[j],b[i]=b[i],b[j]
            a[j],a[i]=a[i],a[j]
print(a)
