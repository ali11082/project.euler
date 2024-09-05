#تعیین افراد مجاز برای شرکت در تیم کبدی
# شرایط:بیش از دو سال در مسابقات شرکت نکرده باشند
# تیم سه نفره از اعضای پیشنهادی ایجاد شود

l=[]
def inte (x):
    i1=int(x)
    return i1
    
n=int(input("insert number of players: "))

s1=str(input("enter the number of round each player has played in the tournament: "))
l1=s1.split()
l11=list(map(inte,l1))
#print(l11)
l2=list(filter(lambda x:x<3,l11))
i2=len(l2)
i3=i2/3
i4=int(i3)
print("number of gruops that can be formed: ",i4)
#print(n)
#print(s1)
#print(l1,l2)
