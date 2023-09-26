s=[]
while a:=input():
    s.append(eval(a))
w=len(s)



for i in range(w):
    for j in range(i+1,w):
        s[i][j],s[j][i]=s[j][i],s[i][j]
    
for el in s:
    print(*el)
    
