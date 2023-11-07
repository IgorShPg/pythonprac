class A:
    def __str__(self):
        return "A"

class B(A):
    def __str__(self):
        return super().__str__()+":B"

class C(B):
    def __str__(self):
        return super().__str__()+":C"

c=C()
print(c)
b=B()
print(b)
a=A()
print(a)
