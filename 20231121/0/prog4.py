import pickle

class C:
    def __init__(self,i):
        self.var=i
c=C(2)
print(len(pickle.dumps(c)))
