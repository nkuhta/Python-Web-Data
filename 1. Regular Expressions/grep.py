########################################################################
#####################           grep        ############################
########################################################################

#   Simulate grep Unix command

#   Regular expression library
import re

inp=input('Enter a regular expression: ')

count=0

fhand=open('mbox.txt','r')

# print('%s'%(inp))

for line in fhand:
    if re.search(inp,line):
        count+=1

print('mbox.txt had %d lines that matched %s'%(count,inp))
