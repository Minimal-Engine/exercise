# Use the file emerson_self-reliance.txt and python with the re-module to solve the following questions:
# original challenge see: https://www.linkedin.com/learning-login/share?account=2163266&forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Flearning-regular-expressions-2%2Fchallenge-character-sets%3Ftrk%3Dshare_video_url%26shareId%3DDTbnKbe7Rx6vSlSzZnHlWQ%253D%253D
# LinkedIn Learning Account required.
import re 
import os

fh =open('emerson_self-reliance.txt')
os.system("cls")
count = 0
for line in fh:
    count +=1
# Match both "lives" and "lived" 
    if re.search("live[sd]", line):
        print ("Treffer für lives oder lived in Zeile:", count)
        #print(line)
# Match "virtue" but not "virtues"
    if re.search("virtue[^s]", line):
        print ("Treffer für virtue in Zeile:", count)
# Match the numbers and periods on all numbered paragraphs
    if re.search("\d\.", line):
        print ("Treffer für Zahl mit anschließendem Punkt in Zeile:", count)
        print (re.findall("\d\.", line))
# Find the 16-Character word thatt starts with "c"
    if re.search("c\w{15}", line):
        print ("Treffer für 16-stelliges Wort, das mit c beginnt in Zeile:", count)
        print (re.findall("c\w{15}", line))