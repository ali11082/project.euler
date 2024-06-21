#امتیازهای کسب شده یک تیم وارد می شود و از آن تعداد برد وباخت تیم خروجی داده می شود
ev=0
#emtiaz_vorodi=ev
je=0
#jame_emtiaze=je
t=0
#tedad_bazi=t
w=0
#tedad_bord=w
d=0
#tedad_mosavi=d
l=0
#tedad_bakht=l


while t<=10:
    ev=int(input("emtize bazit chan shode ro vared kon: "))
    je=ev+je
    t=t+1
    if ev==3:
        w=w+1
    elif ev==1:
        d=d+1
    elif ev==0:
        l=l+1
    print("jame_emtiaze: ",je)
    print("tedad_bazi: ",t)
    print("tedad_bord: ",w)
    print("tedad_mosavi: ",d)
    print("tedad_bakht: ",l)