class C:
    @property
    def field(self):
        if self._val==42:
            print("Secret value")
            return -1
        else:
            return self._val
    
    @field.setter
    def field(self,value):
        if value > 128:
            print("Too old")
            return ValueError
        else:
            self._val=value

    
