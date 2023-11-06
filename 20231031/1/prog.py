import sys

class Omnibus:
    help={}
    def __getattr__(self,val):
        if not val.startswith("_"):
            return len(self.help[val])
    def __delattr__(self,val):
        if self in self.help.get(val,set()):
            self.help[val]-={self}
    def __setattr__(self,val,mean):
        if not val.startswith("_"):
            self.help.setdefault(val,set())
            self.help[val].add(self)

exec(sys.stdin.read())
