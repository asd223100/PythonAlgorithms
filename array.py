from array import array

x = array("i", [5, 15, 25, 35, 45])
print(x)
x.insert(2, 100)
print(x)
print(x[0])
for data in x:
    print(data)
x.remove(25)
print(x)