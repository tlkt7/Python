list1=[1,2,1,2,100,100,100,1]
a=dict()

for i in list1:
    if i not in a:
        a[i]=0
    a[i]+=1
print(a)