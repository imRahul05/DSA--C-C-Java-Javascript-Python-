import bisect

def add(l,x):
    bisect.insort(l,x)
    return l

l= list(map(int,input("Enter the list separated by spaces").split()))
n = int(input("enter the number to insrt into the list"))

list= add(l,n)
print("Sorted list :" , list)