#استاندارد کردن کلمه با کوچک کردن حروف و بزرگ کردن حرف اول
t=0
while t!=10:
    t+=1
    a=input("please enter your name:   ")
    a=a.lower()
    b=a[0]
    b=b.upper()
    a=a.replace(a[0],b)
    print(a)
    
