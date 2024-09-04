#از عدد ورودی اعداد 1و2و3 را شناسایی می کند و سپس
# جمع اعداد 1 تا 3 را می نویسد و آنها را از کوچک به بزرگ سورت میکند
a=input("enter the number:  ")
l=len(a)
def detect (p):
    t=0
    while(t!=l):
        x=a.find(p,t,t+1)
        t=t+1
        if x!=-1:
            x2="+"+a[x]
           # print(x2,end=" ")
            yield x2
g=detect("1")
g2=detect("2")
g3=detect("3")
for i in g:
    print(i,end=" ")
for i in g2:
    print(i,end=" ")
for i in g3:
    print(i,end=" ")
#print(g,g2,g3)



