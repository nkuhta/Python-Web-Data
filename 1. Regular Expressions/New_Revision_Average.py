
#  Calculte the average value from 'New Revision:  39772' type strings


import re

fname=input("Enter file name: ")
fhand=open(fname)

avg=list()

for line in fhand:
    if line.startswith('New Revision:'):
        y=re.findall('[0-9]+',line)
        #print(y,len(y))
        if len(y)==1:
            y=float(y[0])
            avg.append(y)


print(sum(avg)/len(avg))
