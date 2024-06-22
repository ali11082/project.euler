#بزرگترین مقسوم علیه اول عدد رو میده
def prime (n):
    aval=True
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            aval=False
    return aval
l1=[]
def m_p (n): 
    for i in range (2,int(n/2)+1):
        if prime(i)==True and n%i==0:
          #  print(i)
            l1.append(i)
            print(l1[-1])                 
 #   return l1[-1]
v= int(input("please enter the number:   "))
print (m_p(v))
