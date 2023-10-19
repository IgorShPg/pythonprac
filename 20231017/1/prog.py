import string

s=input()
s=s.lower()
sim=set()
for i in range(1,len(s)):
    if s[i-1].isalpha() and s[i].isalpha():
        d=[s[i-1]+s[i]]
        sim=sim.union(set(d))
print(len(sim))
