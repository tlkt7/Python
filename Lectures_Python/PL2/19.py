set1=set()
set1.add(1)
set1.add(2)
set1.add(3)

try:
    set1.remove(10) #set1.remove(10) KeyError: 10, ловит exception
except Exception as arg:
    print("Eror", str(arg))
print("hello world")
print(set1)