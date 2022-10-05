class Fib:
    def __init__(self,limit):
        self.limit=limit

    def __iter__(self):
        self.x=0
        self.y=1
        return self
    
    def __next__(self):
        if self.x+self.y>self.limit:
            raise StopIteration

        x,y=self.x, self.y
        self.x, self.y = self.y, self.x+self.y
        return x+y

a=Fib(1000)
for i in a:
    print(i)

