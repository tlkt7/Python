def f(x):
    return x%2==0

list1=[2,3,5,8,16,19,20]    

list2=list(filter(f,list1))
print(list2)