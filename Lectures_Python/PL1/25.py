cars=["Ford", "Volvo", "BMW"]
x=cars[0]
cars[0]="Toyota"
cars.append("Honda")
t=len(cars)
for x in cars:
    print(x)
    
print(t)