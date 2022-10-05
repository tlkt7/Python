list1=[2,3,5,6,8,9,10]

list2=list(filter(lambda x: x%2==0, list1))
print(list2)