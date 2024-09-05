#وابسته به اینکه تعداد حروف بزرگ و کوچک
#کلیه حروف کلمه را بزرگ و کوچک کند
a=input("please enter the name:    ")
a1=["a","b,","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
a2=['A','B','C',"D",'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
t=0
t1=0
t2=0
l=len(a)
for i in range(0,l):
    b=a[i]
    if b in a1:
        t1=t1+1
    elif b in a2:
        t2=t2+1
if t1>t2:
    a=a.lower()
else:
    a=a.upper()
print(a)
