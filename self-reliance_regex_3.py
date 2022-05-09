import re 
import os


fh =open('emerson_self-reliance.txt')
os.system("cls")
count = 0


for line in fh:
    count +=1
    #print(line)

#match: self, himself, herself, itself, myself, yourself,thyself
    a1 = re.search("\S{0,4}self", line)
    if a1 != None:
        print( "match for self in line",count,":",a1)
#match both: "virtue", and "virtues"
    a2 = re.search("virtue[s]?", line)
    if a2 != None:
        print( "match for virtue in line",count,":",a2)
#Use quantified Repetition to find the word that starts with "T" and has 12 letters
    a3 = re.search("T[\w\S]{11}", line)
    if a3 != None:
        print( "match for T in line",count,":",a3)
#find all text that is inside quotation marks
# /"(.|\n)+?"/g is the answer, didn#
    a4 = re.search('"(.|\n)+?"', line)
    if a4 != None:
        print( "match for quoted Text in line",count,":",a4)