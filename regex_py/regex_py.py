#Watch the following regex video and complete the program below by 
#specifying the regular expression on line #43 in order to define
#strings over {a,b,c,d,...,z} that do not end with the symbol they start with. 

#Note that some exemplary members and nonmembers are given as multiline strings.
#Also note that line #39 denotes the empty string

#The video link is here:
#https://www.youtube.com/watch?v=K8L6KVGG-7o

#Your homework consists of the steps outlined as follows:
#Step-1: Record a 10-minute video tutorial explaining each line of the program below
#(of course with emphasis on the regular expression, how you came up with it)

#Step-2: You can put the video on your drive and share the link. 
#Submit your link on Blackboard. 
#If the link does not work (not properly shared), then you automatically lose 50 pts.

#I suggest you check whether the link works or not by 
#trying to open the link from another (logged-off) browser

#Step-3: Submit audio transcription of your video tutorial. 
#You can do the trancription manually 
#or use a service/program to do that and then go over the transcript and correct it
#If the transcription is not submitted, then you automatically lose 50 pts.

import re

members = '''aaabbcz
zba
ccb
cbbbba'''

nonmembers = '''aba
a
b
c
d

cccbbbbbbac
aaaaba'''

pattern = re.compile(r'^([\w]).*(?<!\1)$', re.MULTILINE)
#let us check if only the member strings are matched with the expression
matches = set([x.group(0) for x in pattern.finditer(members+'\n'+nonmembers)])

print(matches == set(members.split('\n')))