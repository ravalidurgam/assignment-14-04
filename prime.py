a=[]
for x in range(50,100):
    for i in range(2,int(x/2)+1):
        if x%1==0:
            break
    else:
        a.append(x)
print x