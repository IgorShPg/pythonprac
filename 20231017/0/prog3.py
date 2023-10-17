from collections import Counter


C=Counter("fu4hfu4fu4hu4h")
print(C)
C.update(Counter("hebhebhebe"))
print(C)
print(C.most_common())

s=input().split(' ')
print(Counter(s))
