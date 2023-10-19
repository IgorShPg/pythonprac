import string
ln=eval(input())
d={}
strok=""
v=[]
s=input()
while len(s)>1:
    for i in range(0,len(s)):
        if s[i].isalpha()==False:
            strok+=' '
        else:
            strok+=s[i]
    s=input()
strok=strok.lower()
strok = strok.split()
for i in strok:
    if len(i)==ln:
        d[i]=d.setdefault(i,0)+1
if len(d) > 0:
    key = list(d.keys())
    val = max(d.values())
    key.sort()
    print(*[i for i in key if d[i]==val])
    

