lines=[i for i in input() if i!='\r']
l=len(lines)-2
obj=[i for i in input() if i!='\r']
gas=0
liquid=0
while obj!=lines:
    if obj[1]=='.':
        gas+=l
    elif obj[1]=='~':
        liquid+=l
    obj=[i for i in input() if i!='\r']
ever=gas+liquid
height=ever//l

print('#'*(height+2))
for i in range(gas//height):
    print(f"#{'.'*height}#")


for i in range(l-gas//height):
    print(f"#{'~'*height}#")
print('#'*(height+2))
if liquid > gas:
    ll=20
    gl=round(20*gas/liquid)
    skokl=f"{liquid}/{ever}"
    skokg=f"{gas}/{ever}"
    ls=f"{'~'*ll}{skokl}"
    gs=f"{'.'*gl}{' '*(len(ls)-gl-len(skokg))}{skokg}"
else:
    gl=20
    ll=round(20*liquid/gas)
    skokl=f"{liquid}/{ever}"
    skokg=f"{gas}/{ever}"
    gs=f"{'.'*gl}{skokg}"
    ls=f"{'~'*ll}{' '*(len(gs)-ll-len(skokl))}{skokl}"
print(gs)
print(ls)
