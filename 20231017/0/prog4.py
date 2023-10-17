import timeit
from collections import Counter


def wordcounter(s):
    return Counter(s.split(' '))

def worddic(s):
    dic={}
    for i in s.split(' '):
        dic[i]=dic.setdefault(i,0)+1
    return dic

s=input()
lc,tc=timeit.Timer(lambda:wordcounter(str)).autorange()
ld,td=timeit.Timer(lambda:worddic(str)).autorange()
print(lc/tc,ld/td,sep='\n')
