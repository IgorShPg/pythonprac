

class Asker:
    @staticmethod
    def askall(lst):
        for i in lst:
            return i.report()



class Sender:
    count=1
    def report(self):
        if self.__class__.count==1:
            self.__class__.count+=1
            return "Greetings"
        else:
            return "Get away!"

for i in range(3):    
    print(Asker().askall([Sender() for i in range(3)]))
