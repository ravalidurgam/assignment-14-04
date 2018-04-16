a=[10,20,[30,40,50],70,80,90]
b=a
b[0]=1
print a
print b
a[0]=2
print a
print b
import copy
a[2][0]=3
print a
b=copy.copy(a)
print b
a=[10,20,[30,40,50],70,80,90]
b=copy.deepcopy(a)
a[2][1]=4
print a
print b
b=copy.copy(a)
a[3]=5
print a
print b
b=copy.deepcopy(a)
a[4]=6
print a
print b
b=a
a.extend([60,15,25])
print a
print b
a=b
b.extend([35,45])
print a
print b
b=copy.deepcopy(a)
b.extend([55,65])
print a
print b



