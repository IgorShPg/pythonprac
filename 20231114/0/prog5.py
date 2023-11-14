class Decs:
    def __get__(self,obj,cls):
        print("GET",obj,cls)
        return obj._val
    def __set__(self,obj,val):
        obj.val=val

    

class C:
    field=Decs()

    
c=C()
c.data=123
print(c.data)
