a=1
b=2
c=a
a=b
b=c
print(a,b)

a=4
b=5
c=a
a=b
b=c
print(a,b)

#function
def swap(a,b):
    c=a
    a=b
    b=c
    return a,b

print(swap(1,2))
print(swap(4,5))