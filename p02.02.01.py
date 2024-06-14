#سن افراد برای ثبت نام گرفته می شود و مشخص میشود که بزرگترین سن برای چندمین ثبت نام است؟
s=19
bs=19
t=0
while s!=-1:
    s=int(input("senetoon ro vared konid jenab, (sen mojaz = beyn 20 ta 901!) :   "))
    if bs<=s:
        bs=s
        t=t+1
    elif (s>90)or(s<20):
        print("senetoon dar mahdode mojaz nis")
    print("bishtarin sen: ",bs,"ke marboot be nafare: ",t," hast")