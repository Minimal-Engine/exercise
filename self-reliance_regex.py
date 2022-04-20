# Use the file emerson_self-reliance.txt and python with the re-module to solve the following questions:
# original challenge see: https://www.linkedin.com/learning-login/share?account=2163266&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Flearning-regular-expressions-2%2Fchallenge-characters%3Ftrk%3Dshare_video_url%26shareId%3DZg5DDeybTDaLUyC9kgb%252Feg%253D%253D
# LinkedIn Learning Account required.
import re 
import os

x = list()
y = list()
z = list()
a1 = 0
a2 = {"himself":0,"herself":0,"itself":0,"myself":0,"yourself":0,"thyself":0}
a3 = list()
a4 = list()
fh =open('emerson_self-reliance.txt')
os.system("cls")

for i in fh:
# 1. how many times does the word "self" appear? (! case insensitive)
    x = re.findall('self', i, re.IGNORECASE)
    a1 = a1 + len(x)
# 2. count the words: himself,herself,itself,myself,yourself,thyself
    for k in a2.keys():
        count = re.findall(k, i, re.IGNORECASE)
        a2.update({k: a2[k] + len(count)})
# 3. using three literal characters and three wildcards try matching the following words: please, palace, parade
    y = re.findall('p..a.e', i, re.IGNORECASE)
    a3 = a3 + y
# 4. what matches /t..ch/ besides teach?   
    z = re.findall('t..ch', i, re.IGNORECASE)
    a4 = a4 + z

print ("Die Antwort auf Frage 1 ist:",a1)
print ("Die Antwort auf Frage 2 ist:", a2)
print ("Die Antwort auf Frage 3 ist:", a3)
print ("Die Antwort auf Frage 4 ist:", a4)