#اعدادی را به عنوان ورودی میگیرد و آنکه بیش ترین مقسوم عبیه را دارد را خروجی می دهد
t=0
a=0
t2=0
x=0
bs=0
def maqsoom (x):
    t=0
    m=1
    for i in range (m,x):
        n=x%i
        if n==0:
            t=t+1
            print("maqsoom elayh: ",i)
    return    t



while t2<=20:
    x=int(input("ye adad vared kon: "))
    s=maqsoom(x)
   # print(s)
    if bs<=s:
       bs=s
    print(bs)
    t2=t2+1   


   

    
       
            
            
            
       
   
        
