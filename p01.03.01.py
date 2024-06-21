#بزرگترین مقسوم علیه اول عدد رو میده
def prime (n):
    aval=True
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            aval=False
    return aval
def m_p (n):
    for i in range (int(n/2)+1,1,-1):
        if (n%i==0) and (prime(i)==True):
            return i
v= int(input("please enter the number:   "))
print (m_p(v))
