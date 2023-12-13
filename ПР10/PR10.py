from random import randint
n=int(input())
m=int(input())
a=[]
for i in range(n):
    b=[]
    for j in range(m):
        b.append(randint(1,100))
    a.append(b)
f=open('ФИО_группа_vivod.txt','w')
for i in a:
    for j in i:
        f.write(str(j))
        f.write(' ')
    f.write("\n")
f.close()
f=open('ФИО_группа_vivod.txt','r')
b=[]
for i in f:
    c=[]
    s=i.split()
    for j in s:
        c.append(j)
    b.append(c)
f.close()
for i in b:
    mn=i.index(min(i))
    mx=i.index(max(i))
    i[mx],i[0]=i[0],i[mx]
    i[mn],i[-1]=i[-1],i[mn]
f=open('ФИО_группа_vivod.txt','w')
for i in b:
    for j in i:
        f.write(str(j))
        f.write(' ')
    f.write("\n")
f.close()