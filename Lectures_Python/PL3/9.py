class Person:

    def __init__(self,name,surname):
        self.name=name
        self.surname=surname

    def show(self):
        print(f'{self.name}-{self.surname}')
        #print("{1}-{0}".format(self.name, self.surname))

    def __str__(self):
        return f'{self.name}-{self.surname}'

a=Person("Ibrahhim", "Tlektes")
b=Person("Daniel", "Tlektes")

print(a)
print(b)