#تشخیص حروف یک کلمه و چیدن حروف آن کلمه در کنار یکدیگر

a=input("Hello....")
b=a.find("h")
c=a.find("e")
d=a.find("l")
e=a.find("l",d+1)
f=a.find("o")
if b<c<d<e<f:
    print("hello")