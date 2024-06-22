#جمع اعداد اول زیر2000000
l1=[]
def prime (n):
    aval=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            aval=False
            break
    return aval

def co (n): 
    counter=0        
    for i in range(2,n):
        if prime(i):
            l1.append(i)
            print(i)
            counter+=1
    print(sum(l1))
        
print (co(2000000) )      
#print(prime(7))        
        
