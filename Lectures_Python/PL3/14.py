x=100 #глобальная переменная

def f(): #локальная
    x=200
    print(x)

f()
print(x)