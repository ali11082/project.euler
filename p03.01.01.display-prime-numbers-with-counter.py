#نمایش اعداد اول به همراه شمارنده

def prime (n):
    aval=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            aval=False
            break
    return aval

def co (n): 
    counter=0        
    for i in range(1,n):
        if prime(i):
            counter+=1
            print(i,prime(i),counter)
        
print (co(100) )      
#print(prime(7))        
        
