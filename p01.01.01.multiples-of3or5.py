#!/usr/bin/python3
#مجموع ضریب سه و پنج زیر هزار
def zarib (n):
    c=0
    for i in range (0,n):
        if (i%3==0)or(i%5==0):
            c=c+i
    return c    
output=zarib(1000) 
print(output)      
