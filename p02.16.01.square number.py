#جذر عدد را میگیرد و بدون رند کردن آن را با 4 رقم اعشار نمایش می دهد
 
n=0
n=int(input("enter number of inputs number: "))
for i in range(0,n):
    #print(i)
    n1=float(input("enter the number: "))
    from math import sqrt
    n2=("{:.5f}".format(sqrt(n1)))
    n3=float(n2)
    n4=n3-(((n3*100000)%10)/100000)
    n5=("{:.4f}".format(n4))
   # print(type(n2),n2)
   # print(type(n3),n3) 
   # print(type(n4),n4)
   # print(type(n5),n5)
    print("The square root of your number with 4 decimal places is: ",n5)
    
