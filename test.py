x = int(input("x "))
y = int(input("y "))

for i in range(0,y):
    x = (48271*x)%(2**31-1)
    
print(x)