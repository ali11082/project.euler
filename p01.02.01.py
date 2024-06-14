#!/usr/bin/python3
#مجموع اعداد زوج دنباله فیبوناچی
def zoj (n):
    if n%2==0:
        return n

def fibo (n):
    l1=[1,2,3]
    c=3
    while int(l1[-1]<n):
        s=(int(l1[-2])+int(l1[-1]))
        l1.append(s)
        c=c+1
    return l1    
#print(fibo (40))           

l3=[]
def oy (n):
    for i in fibo(n):
        if i==zoj(i):
            l3.append(i)
            s=sum(l3)
    return s#,l3
          
    
print(oy(4000000))

    
 
