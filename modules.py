# import the library
import urllib
from mypackage import myfunction
# use it
myfunction.myfunction()
urllib.urlopen("http://www.google.com")
print dir(urllib)

help(urllib.urlopen)
help(urllib.FancyURLopener)

# In this exercise, you will need to print an alphabetically sorted list of all functions in the re module, which contain the word find.
import re

# Your code goes here
newlist = []
for x in dir(re):
    if "find" in x:
        newlist.append(x)
print newlist
