##پیدا کردن کالایی در بین کالا ها که به صرفه تر باشه
#اول تعداد کالا گرفته می شود
#بعد نمره قیمت و بعد در ادامه کیفیت اون کالا گرفته میشود
#در صورتی که یک کالا با کیفیت بهتر و قیمت کمتر پیدا شد میگوید آفرین 
#

def inte (x):
    i2=int(x)
    return i2
n=int(input("enter the number of laptops:"))
s1="t"   
i3=0
#while s1!="end":
for i in range(0,n):
    s1=str(input("first enter  the price  and then quality:  "))
    l1=s1.split()
    #print(l1)
    l2=list(map(inte,l1))
   # print(l2)
    i1=l2[0]
    i2=l2[1]
    if i1>=i2:
        i3+=1
if i3>0:
    print("bravo!")
else:
    print("sorry.good try!")   
#print(i1)
#print(l2)
#print(l3)