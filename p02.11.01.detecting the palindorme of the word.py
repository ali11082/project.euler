#تعیین پالیندورم بودن کلمه

a=input("please enter the word:    ")
t=0
t1=0
t2=0
l=int(len(a))
for i in range(0,l):
    b=a[i]
    c=a[-i-1]
    if b==c:
        d="pailndrome"
    else:
        d="not pailndome"
print(d)
