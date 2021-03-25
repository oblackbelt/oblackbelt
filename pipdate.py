#!/usr/bin/python
# *-* encoding utf-8 *-*

import os #imports

print ("Starting Update Process") #print bogus message

os.system("touch lista.txt") #if exists, touch, if not, create.
os.system("rm lista.txt") #Now delete (why touch? avoid error here...)
os.system("sudo pip list --outdated >> lista.txt") #get list and write file

with open ("lista.txt", "r") as f: #open read only in f
    wordlist = [line.split(None, 1)[0] for line in f] #pick only first word each line

wordlist2=wordlist[2:] #Removes title and ------ lines
print (wordlist2) #shows whole list

#Now do the magic
for i in wordlist2: print(os.system("sudo pip install --upgrade " + i))

print ("Process is done, 0 means OK, 1 means not-OK...") #kiss goodbye

#end of story.
