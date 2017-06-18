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

########################################################################
###################           re.search()         ######################
########################################################################

#   Returns true or false

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
print('*******    ^X-\S+: = start with X- and match at least one non-whitespace until a :      *****************')
print()
hand=open('mbox-short.txt')

for line in hand:
    line=line.rstrip()
    #   re.search returns true or false, ^From: means startswith 'From:'
    if re.search('^X-\S+:',line):
        print(line)

print()
print('*******    ^From:.+@ = start with "From:" have an @ sign      *****************')
print()
hand=open('mbox-short.txt')

for line in hand:
    line=line.rstrip()
    if re.search('^From:.+@',line):
        print(line)

########################################################################
##################           re.findall()         ######################
########################################################################
print()
print('*************  re.findall()  *********************')

x= 'My 2 favorite numbers are 19 and 42'
#   all items with 1 digit or more
y = re.findall('[0-9]+',x)
print(y)

#   Find all sequences with one or more uppercase vowels
y = re.findall('[AEIOU]+',x)
print(y)

#   GREEDY MATCHING
x='From: Using the : character'
#   Starts with F and ends with : and has the largest number of characters in between
y=re.findall('^F.+:',x)
print(y)

# NON GREEDY matching
x='From: Using the : character'
#   Starts with F and ends with : and has the SMALLEST number of characters in between because of ?
y=re.findall('^F.+?:',x)
print(y)

#  More advanced findall()

x = 'From steph.marquard@uct.ac.za Sat Jan 5 09:04:16 2008'
#y = re.findall('\S+@\S+',x)
y = re.findall('^From (\S+@\S+)',x)
print(y)

fhand=open('mbox-short.txt')
for line in fhand:
    if line.startswith('From '):
        y=re.findall('^From (\S+@\S+)',line)
        print(y)

#  Pull out the email domain.
x = 'From steph.marquard@uct.ac.za Sat Jan 5 09:04:16 2008'
#   match a single non-blank character after @ until you find a blank
y=re.findall('@([^ ]*)',x)
print(y)

########################################################################
##################         Spam Confidence        ######################
########################################################################
print()
print('*************  Spam Confidence  *********************')

hand=open('mbox-short.txt')
numlist=list()

for line in hand:
    line=line.rstrip()
    #   Start with X-DSPAM-Confidence:
    #   start extracting character 0 through 9 or period "."
    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) !=1: continue
    num = float(stuff[0])
    numlist.append(num)

print('Max = ',max(numlist))

########################################################################
##################         Escape character        #####################
########################################################################
print()
print('*************  \Escape character  *********************')

x = 'We just received $10.00 for cookies'
#   Find all \$ real dollar sign elements with "." or digits after it until a space
y = re.findall('\$[.0-9]+',x)
print(y)
