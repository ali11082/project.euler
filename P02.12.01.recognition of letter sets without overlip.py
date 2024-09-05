#تشخیص وجود دو مجموعه حرف 
#ABو BA 
#بدون هم پوشانی  در کلمه  
t=0
z1=0
z2=0
t2=0
g1=0
g2=2
a=input("please enter the word:  ")
l=len(a)
while(t!=l):
    x1=a.find("A",t,t+1)
    y1=a.find("B",t+1,t+2)
    t=t+1
    if (x1!=-1)and(y1!=-1):
        z1=t
        g1=1
while(t2!=l):
    x2=a.find("B",t2,t2+1)
    y2=a.find("A",t2+1,t2+2)
    t2=t2+1
    if (x2!=-1)and(y2!=-1):
        z2=t2
        g2=1
if (z1+1!=z2)and(g1==g2):
    print("OK")
elif (z1+1==z2)and(g1==g2):
    print("overlab")
else:
    print("not")
  