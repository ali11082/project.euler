#جمع ارقام عدد 2 به توان 1000
p=(pow(2,1000))
s=0
while p>=1:
    b=p%10
    s=s+b
    p=p//10         
print("s=",s)   


