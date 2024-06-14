




a=0
import random
h1=0
h2=99
#h=random.randint(h1,h2)
r="felan hichi"
#print("man hadsam =",h, " bood")
#r=input("age adadam bozorgtare benevis b va age hadsam koochiktar boodesh benvis k va age dorost goftam benevis ok:   ")
while (r!="ok"):
    h=random.randint(h1,h2)
    print("man hadsam =",h," chetore?")
    r=input("age adadam bozorgtare benevis b va age hadsam koochiktar boodesh benvis k va age dorost goftam benevis ok:   ")
    if r=="ok":
        print("belakhare toonestam")
    elif r=="k":
        h1=h+1    
    elif  r=="b":
        h2=h-1
    else:
        print("vorodit motabar nabood pas adad jadid hads mizanam")
#if r=="ok":
 #   print("tamam tamam")