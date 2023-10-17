import string

g=set("aeyuio")
s=set("qzwsxdcfrvgtbhjnmklp")
strok=set(input())
g=g&strok
s=s&strok
print(len(g))
print(len(s))
