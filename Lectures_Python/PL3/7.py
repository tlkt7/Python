#double all elements in list(using map)

list1=[2,5,6,10,100,202]

list2=list(map(lambda x: x*2, list1))
list3=list(map(lambda x: x**2, list1))

print(list2)
print(list3)