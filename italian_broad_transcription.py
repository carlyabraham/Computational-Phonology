# -*- coding: utf-8 -*-
"""
@author: carly

NOTE: When running, you will be prompted for the file name to process (make sure 
the text file is in the same location as the .py file). Just give the file 
name (no ".txt") and press enter.
"""


#open input file
import re
filename = input("give the file name: ")
with open(filename+'.txt','r', encoding='utf-8') as inf:
    #get text to string
    text = inf.read()

#remove stress accents from vowels for processing
text = text.replace('à', 'a')
text = text.replace('è', 'e')
text = text.replace('é', 'e')
text = text.replace('ò', 'o')
text = text.replace('ù', 'u')
    
#create tuples list of italian to ipa, using regex to identify environments where rules take place
    #the ordering of the tuples is intentional to mimic ordering of rules to get the desired output
italianTrans = [
        (r'sc([ie])', r'ʃ\1'), #sc becomes ʃ before i or e
        (r'sc[h]?', r'sk'), #sc becomes sk elsewhere
        (r'ʃi([aeiou])', r'ʃ\1'), #sci becomes ʃi before another vowel
        (r'c([aou])',r'k\1'), #c is k before back vowels
        (r'c([ei])',r'ʧ\1'),#c is ʧ before non-back vowels
        (r'cʧ', r'ʧʧ'), #cci is ʧʧi, etc
        (r'([ʧ])i([aeiou])', r'ʧ\2'), #ci is ʧ before another vowel
        (r'gi([aeiou])', r'ʤ\1'), #gi is ʤ before another vowel
        (r'ng([ie])', r'nʤ'), #ng becomes nʤ before front vowels (handle before elsewhere (before velars))
        (r'gh([ie])', r'g\1'), #gh becomes g before front vowels
        (r'gli([aeiou])', r'ʎ\1'), #gli is ʎ before another vowel
        (r'gli', r'ʎi'), #gli is ʎi elsewhere
        (r'[c]?ch([ie])', r'k\1'), #ch (or cch?) becomes k before front vowels
        (r'gn', r'ɲ'), #gn becomes ɲ
        (r'n([gk])', r'ŋ\1'), #n becomes ŋ before velars
        (r'qu', r'kw'), #qu is kw
        (r'\bh', ''), #h is silent word-initial
        (r'z', r'ʦ'), #z is pronounced as ʦ
        (r'([aeiou])s([aeiou]|[bdg])', r'\1z\2'), #s becomes z intervocalically or word-initially
        (r'([aeiou])ss([aeiou])',r'\1s\2') #ss is just pronounced as s
        ]


#loop through every character in txt string
for i in italianTrans:
    text = re.sub(i[0], i[1], text)
    
#print(text)
with open(filename+'_ipa.txt', 'w', encoding='utf-8') as outf:
    outf.write(text)    