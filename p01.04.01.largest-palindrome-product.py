#بزرگترین عدد شش رقمی که از دو طرف یک عدد خوانده بشه  و حاصلضرب سه عدد دو رقمی باشه
#i1=int(input("enter count number:  "))
l1=[]

for i in range(100,1000):
        for j in range (100,1000):   
            h=i*j
            if h>=100000 :
                s=str(h)
                if (s[0]==s[5]) and (s[1]==s[4])and (s[2]==s[3] )  :
                    l1.append(s)
                    i2=max(l1)
                    print(i2)
        





        