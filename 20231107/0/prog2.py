class A:
    def __init__(self,var):
        self.var=var

class B(A):
    def __init__(self,var):
        super().__init__(var)
        self.otver=var*2
b=B(12)
print(b.var)
print(b.otver)
