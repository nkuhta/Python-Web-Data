########################################################################
###############           Regular Expressions         ##################
########################################################################

#   regex or regexp
#   Really clever "wild card" Expressions for matching/parsing/extracting
#   Smart find or search

#   Import Regular Expression Library
import re

#   use re.search() like find()

hand=open('mbox-short.txt')

for line in hand:
    line=line.rstrip()
    if line.find('From:') >=0:
    #if line.startswith('From:'):
        print(line)

print('****')
hand=open('mbox-short.txt')

for line in hand:
    line=line.rstrip()
    #   re.search returns true or false
    if re.search('From:',line):
        print(line)

print('****           ^ = startswith      *****************')
hand=open('mbox-short.txt')

for line in hand:
    line=line.rstrip()
    #   re.search returns true or false, ^From: means startswith 'From:'
    if re.search('^From:',line):
        print(line)

print()
print('*******    ^X.*: = start with X and match any character any that any number of times until a :      *****************')
print()
hand=open('mbox-short.txt')

for line in hand:
    line=line.rstrip()
    #   re.search returns true or false, ^From: means startswith 'From:'
    if re.search('^X.*:',line):
        print(line)

print()
print('*******    ^X-\S+: = start with X- and match at least one non-black until a :      *****************')
print()
hand=open('mbox-short.txt')

for line in hand:
    line=line.rstrip()
    #   re.search returns true or false, ^From: means startswith 'From:'
    if re.search('^X-\S+:',line):
        print(line)

########################################################################
##################           re.findall()         ######################
########################################################################
print()
print('*************  re.findall()  *********************')

x= 'my 2 favorite numbers are 19 and 42'
#   all items with 1 digit or more
y = re.findall('[0-9]+',x)
print(y)
