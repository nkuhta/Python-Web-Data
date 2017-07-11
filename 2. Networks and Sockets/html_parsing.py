########################################################################
################           Understanding HTML        ###################
########################################################################

import urllib.request
import urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode())

#######################################################################################
###################           Parsing with Beautiful Soup        ######################
#######################################################################################

# import urllib
# from BeautifulSoup import *
#
# url = input('Enter URL')
#
# html = urllib.urlopen(url).read()
# soup = BeautifulSoup(html)
#
# #   Retrieve a list of the anchor tags
# #   Each tag is like a dictionary of HTML attributes
#
# for tag in tags:
#     print(tag.get('href',None))
