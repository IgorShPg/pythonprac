class Rectangle:
    rectcnt=0
    def __init__(self,a,b,c,d):
        self.x1=a
        self.x2=c
        self.y1=b
        self.y2=d
        self.__class__.rectcnt+=1
        setattr(self,f"rect_{self.rectcnt}",self.rectcnt)
    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1}) :{self.rectcnt}"
    def __abs__(self):
        return (self.x2-self.x1)*(self.y2-self.y1)
    def __lt__(self,obj):
        return (self.__abs__())<(obj.__abs__())
    def __eq__(self,obj):
        return (self.__abs__())==(obj.__abs__())
    def __mul__(self,mul):
        return self.__class__(self.x1*mul,self.y1*mul,self.x2*mul,self.y2*mul)
    def __getitem__(self,ind):
        return [(self.x1,self.y1),(self.x1,self.y2),(self.x2,self.y2),(self.x2,self.y1)][ind]
    def __bool__(self):
        return abs(self)!=0
    def __del__(self):
        print("Deleting",self)
        self.__class__.rectcnt-=1


ex=Rectangle(1,2,3,4)
print(ex)
ex1=Rectangle(5,6,7,8)
print(ex1)
ex2=Rectangle(5,6,7,8)
for i in ex2:
    print(i)
print(ex2[2])
print(ex2)
print(ex1*4)

