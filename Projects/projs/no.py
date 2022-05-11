l=[1,5,2,5,2,0]
for i in range(len(l)):
    for j in range(i):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)

