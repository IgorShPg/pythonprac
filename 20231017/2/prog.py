import math

func={}
count=0

while (s:=input().split())[0] != 'quit':
    count+=1
    if s[0][0]==':':
        fname=s[0][1:]
        f=s[-1]
        func[fname]=(f,s[1:-1])
    elif s[0] in func:
        par=func[s[0]][1]
        op=dict(zip(par,map(eval,s[1:])))
        print(eval(func[s[0]][0],math.__dict__,op))

if (len(s)>2):
    string=s[1]+' '+s[2]
    string=string.strip('"').strip("'")
else:
    string=s[1].strip('"').strip("'")
print(string.format(len(func)+1,count+1))
