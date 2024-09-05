#کمترین مسافتی که سه دوست باید از سه نقطه طی کنند

print("enter x location freind & for end write -1000")
l1=[]
f1=0
x=0
l=0
def ave (l):
    le=len(l)
    s=sum(l)
    a=s/le
    return a
def fasele(x):
    f2=x-ave(l1)
    f2=abs(f2)
    return f2   
while f1!=-1:
    f1=float(input("enter the number:...."))
    l=l1.append(f1)
    print(l1)
    print(ave(l1))
    d=list(map(fasele,l1))
    print("distance: ",d)
    s2=sum(d)
    if s2==int(s2):
        print(int(s2))
    else:
        print(s2)    
   # from functools import reduce
   # l2=reduce(lambda f1: x+y)
   # print(l2)    