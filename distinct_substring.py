a=int(input())
b=input().strip()
c=[]
prev=''
subs=''
for i in range(a):
    #prev=''
    #subs=''
    for j in range(i,a):
        if b[j] not in subs:
            subs+=b[j]
        else:
            if(len(subs)>0):
                if subs in prev:
                    prev=subs
                    subs=''
                    break
                    pass
                else:
                    c.append(subs)
                    #print(subs)
                    prev=subs
                    subs=''
                    break
print(*sorted(c))