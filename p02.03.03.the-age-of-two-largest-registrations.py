#دو نفر بزرگ ثبت نام ککنده به همراه شماره ثبت نامشون 
#gofte shode vorodi yekta hast! va tekrari nis
s=19
#bozorgtarin_sen=bs
bs=19
t1=0
bs2=18
t2=0
c=0
while s!=1:
    print("(sen mojaz = beyn 20 ta 901!)")
    s=int(input("senetoon ro vared konid jenab :   "))
    c=c+1
    if bs<=s:
        if bs2<=s:
            bs2=bs
            bs=s
            t2=t1
            t1=c
    elif (bs>s)and(s>=bs2) :
        bs2=s
        t2=c
    elif (s>90)or(s<20):
        print("senetoon dar mahdode mojaz nis")
    if c==1:
        print("bishtarin sen: ",bs,"hast ke marboot be nafare: ",t1," hast")
    else:
        print("bishtarin sen: ",bs,"hast ke marboot be nafare: ",t1," hast") 
        print("va nafare dovom bishtarin sen: ",bs2,"hast ke marboot be nafare: ",t2," hast")