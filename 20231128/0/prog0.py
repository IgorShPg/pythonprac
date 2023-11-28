D=type("C",(),{"var"=100500,"__init__":lambda self,x:setattr(slef,"var",x)})

class Doubeleton(type):
    _instance=[None,None]
    res=cls._instance.pop(0)
    if res is None:
        res=super().__call__(*args,**kw)
    cls._instance.append9](res)
    return res



match input().split():
    case["move", var1,var2]:
        print(f"moving {var2} to {var1}")
    case["push"|"pop" as cmd,*param]:
        print(f"{cmd}ing",*param)
    
    case _:
        print("Parse error")




class C:
    a, b, c=input("a, b, c: ").split()

while s:=input("> "):
    match s.split():
        case[C.a,*other] if "yes" in other:
            print("1")
        case[C.b]:
            print("2")
        case[C.c,*_, C.b]:
            print("3")
