import sys

class Triangle:
    def __init__(self,a,b,c):
        self.x=tuple(a)
        self.y=tuple(b)
        self.z=tuple(c)
    def __abs__(self):
        return abs((self.y[0]-self.x[0])*(self.z[1]-self.x[1])-(self.z[0]-self.x[0])*(self.y[1]-self.x[1]))/2
    def __bool__(self):
        return abs(self)>0
    def __eq__(self,obj):
        return abs(self)==abs(obj)
    def __lt__(self,obj):
        return abs(self)<abs(obj)
    def __le__(self,obj):
        return abs(self)<=abs(obj)
    def __contains__(self,obj):
        if type(obj)==type(tuple()):
            x,y=obj
            x0,y0=self.x
            x1,y1=self.y
            x2,y2=self.z
            a=(x0-x)*(y1-y0)-(x1-x0)*(y0-y)
            b=(x1-x)*(y2-y1)-(x2-x1)*(y1-y)
            c=(x2-x)*(y0-y2)-(x0-x2)*(y2-y)
            return a*b>=0 and b*c>=0 and a*c>=0
        else:
            return obj.x in self and obj.y in self and obj.z in self if obj else True

    def __and__(self,obj):
        def cross(obj,self):
            return not (obj.x in self and obj.y in self and obj.z in self) and (obj.x in self or obj.y in self or obj.z in self)
        return bool(self) and bool(obj) and (cross(self,obj) or cross(obj,self))


exec(sys.stdin.read())
