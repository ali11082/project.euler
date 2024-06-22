#پاک کردن حروف صدا دار
#چاپ نقطه قبل حروف بی صدا
#نوشتن حروف بی صدا به صورت کوچک
h="."
g=str(input("enter the word:  "))
seda=["a","e","i","o","u"]
for i in seda:
    g=g.replace(i,"")
l=len(g)
g=g.lower()
for k in range(0,l):
    s=h+g[k]
    print(s,end=" ")

