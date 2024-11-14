def si(p,r,t):
    s = (p*r*t)/100
    return s

def ci(p,r,t):
    c = (p * (1+r/100)**t) - p
    return c

p = float(input("Enter the princiapl amount"))
r = float(input("Enter the rate of interest"))
t = float(input("Enter the time period in terms of years"))
choice = int(input("Choose any one  option \n 1. Simple Interst \n 2. Compound Interest \n Enter the option : "))

if choice==1:
    a = si(p,r,t)
    print("simple inters",a)
else:
    b = ci(p,r,t)
    print("compound interest" , b)


 