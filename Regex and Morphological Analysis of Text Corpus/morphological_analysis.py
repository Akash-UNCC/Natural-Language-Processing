"""
Problem 1 (Python/NLTK warmup) (5 points). Define a variable funny to contain the string
“colorless green ideas sleep furiously” (from Chomsky’s famous phrase). Now write code to
perform the following tasks:
a. Write a function to split funny into a list of strings, one per word, using Python’s split()
operation.
b. Write a function to extract the second letter of each word in silly and join them into a string and
output that string.
c. Write a function to build a list called phrases consisting of all the words up to (but not
including) sleep in funny.
Hint: use the index() function in combination with list slicing.
d. Write a function to combine the words in phrases back into a single string, using join(). Make
sure the words in the resulting string are separated with whitespace.
e. Write a function to print the words of funny in alphabetical order, one per line
"""

def split_funny( mylist ):
   print(funny.split())

def second_letter(funny):
   i = 0
   s2 = funny.split()
   #print(s2)
   word = ''
   for w in s2:
       temp = s2[i]
       i = i + 1
       word = word + temp[1]
   print("Problem1 (b) Answer  "+word)


def build_a_list(funny):


    k =funny.index('sleep')
    #print(k)
    #print(funny[0:k])
    s3 = funny[0:k]
    #print(type(s3))
    phrases = ''.join(s3)
    print("Problem1 (c) Answer  "+phrases)
    return phrases


def combine_phrases(phrases):
    join_phrase = ''.join(phrases)
    print("Problem1 (d) Answer  "+join_phrase)
    # print(type(s3))

def alpha_order_funny(funny):
    temp = funny.split()
    temp.sort()
    print("Problem1 (e) Answer ")
    for w in temp:
        print(w)

funny = "colorless green ideas sleep furiously"
split_funny(funny)
second_letter(funny)
phrases =build_a_list(funny)
combine_phrases(phrases)
alpha_order_funny(funny)

""""
Problem 2 (Python/NLTK warmup) (3 points). Write a function that takes a sentence expressed
as a single string, splits it and counts up the words. Get it to print out each word and the word’s
frequency, one per line, in alphabetical order.
"""
import nltk
from nltk import word_tokenize

def problem_2(teststring):

     temp = word_tokenize(teststring)
     temp_lower = [w.lower() for w in temp]
     frequency = nltk.FreqDist(temp_lower)
     for w, f in sorted(frequency.items()):
         print(w + " :frequency = " , f)


teststring = 'NLP was the UNCC of learn it CTS the cs of test  it on the ms of NLP it was nlp age of test'
problem_2(teststring)

"""
 Using re.findall(), write a regular expression which
 will extract pairs of values of the form login name@email domain from the following string:
 str = "austen-emma.txt:hart@vmd.cso.uiuc.edu (internet) hart@uiucvmd (bitnet)
 austen-emma.txt:Internet (72600.2026@compuserve.com); TEL: (212-254-5093) .
 austen-persuasion.txt:Editing by Martin Ward (Martin.Ward@uk.ac.durham)
 blake-songs.txt:Prepared by David Price, email ccx074@coventry.ac.uk
"""

import re
test_string = 'austen-emma.txt:hart@vmd.cso.uiuc.edu (internet) hart@uiucvmd (bitnet)... austen-emma.txt:Internet (72600.2026@compuserve.com); TEL: (212-254-5093) ... austen-persuasion.txt:Editing by Martin Ward (Martin.Ward@uk.ac.durham)... blake-songs.txt:Prepared by David Price, email ccx074@coventry.ac.uk'




def extract_pairs(test_string):
      email_address = re.findall(r'[\w\.-]+@[\w\.-]+', test_string)
      for e in email_address:
         print(e.split('@'))

extract_pairs(test_string)

"""
Problem 5 (Python/NLTK/Regex) (10 points). Write a function to eliminate duplicate lines from
an input file. Assume the input file contains strings with alphanumeric characters.
"""
def remove_dup_lines(filename):
     lines_seen1 = set()
     readf = open("infilename1.txt")
     outfile17 = open("outfile17.txt","w")
     for line in readf:
         if line not in lines_seen1:
           lines_seen1.add(line)
           outfile17.write(line)
     readf.close()

remove_dup_lines('infilename1.txt')

""""
Problem 6** (Python/NLTK/Regex) (10 points). What does the following Python program do?
What would be an example input file? What would the output be?
"""
"""
import sys
import re
try: infile = open(sys.argv[1])
except: infile = sys.stdin
for line in infile:
    line = line.strip()
    #print(line)
    if not line or line[0] == '#': break
    parens=re.sub('[^()]','.',line.replace('(','(.').replace(')', '.)'))
    print(parens)
    try:
         matchparens = re.compile(parens)
         print(matchparens)
    except:
        print(sys.stderr, "Error in input")
        continue
    for t in matchparens.match(line).groups():print(t)
"""
"""
Problem 7. (Morphological analysis/Regex/NLTK) (65 points).
a. (15 points) Write a function to load the debate file and assign statements to speakers. There
are three main speakers: Obama, Romney and Lehrer but not statements made by the
speakers begin with the speaker tag. Your function should have a rule to concatenate
statements made by the same speaker. Your code should ignore crosstalk and notes about
audience behavior.
"""
#Write a function to load the debate file and assign statements to speakers. There
#are three main speakers: Obama, Romney and Lehrer but not [ all ]statements made by the
#speakers begin with the speaker tag. Your function should have a rule to concatenate
#statements made by the same speaker. Your code should ignore crosstalk and notes about
#audience behavior.
print("Solution to question 7 (a):::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
import nltk.corpus
#my_corpus = nltk.corpus.PlaintextCorpusReader('debate.txt')
#print(str(nltk.corpus.brown).replace('\\\\','/'))

readfx = open("debate.txt")
# outfile1 = open("outfile1.txt","w")

obama =''
lehrer=''
romney=''
#Preprocessing file by removing crosstalk audiance response and extra data not spoken any speakers
filedata = readfx.readlines()
filedata = [re.sub(r'\(([A-Za-z])+\)', r'',line) for line in filedata]
filedata = [i for i in filedata if i[:-1]]
filedata = [i for i in filedata if re.split('Â',i)[0]]

readf = open("debate.txt")
for line in readf:
    a=line
    b=a.split()
    #print(b)
    if(len(b)==0):
     continue
    else:
        if(b[0]=='OBAMA:'):
            #print(' '.join(b))
            obama =obama+ ' '.join(b)
            for line in readf:
                a = line
                b = a.split()
                # print(b)
                if(b[0]=='LEHRER:' or b[0]=='ROMNEY:'):
                      break
                else:
                    obama =obama+ ' '.join(b)
                    #print(' '.join(b))

print(obama)
""""
readf1 = open("debate.txt")
# outfile1 = open("outfile1.txt","w")


lehrer=''

for line1 in readf1:
    a=line1
    b=a.split()
    #print(b)
    if(len(b)==0):
     continue
    else:
        if(b[0]=='LEHRER:'):
            #print(' '.join(b))
            lehrer =lehrer+ ' '.join(b)
            for line1 in readf1:
                a = line1
                b = a.split()
                # print(b)
                if(b[0]=='OBAMA:' or b[0]=='ROMNEY:'):
                      break
                else:
                    lehrer =lehrer+ ' '.join(b)
                    #print(' '.join(b))
print(lehrer)
"""
readf2 = open("debate.txt")
# outfile1 = open("outfile1.txt","w")


romney=''
for line2 in readf2:
    a=line2
    b=a.split()
    #print(b)
    if(len(b)==0):
     continue
    else:
        if(b[0]=='ROMNEY:'):
            #print(' '.join(b))
            romney =romney+ ' '.join(b)
            for line2 in readf2:
                a = line2
                b = a.split()
                # print(b)
                if(b[0]=='LEHRER:' or b[0]=='OBAMA:'):
                      break
                else:
                    romney =romney+ ' '.join(b)
                    #print(' '.join(b))
print(romney)

readf1 = open("debate.txt")
lehrer=''

for line1 in readf1:
    a=line1
    b=a.split()
    #print(b)
    if(len(b)==0):
     continue
    else:
        if(b[0]=='LEHRER:'):
            #print(' '.join(b))
            lehrer =lehrer+ ' '.join(b)
            for line1 in readf1:
                a = line1
                b = a.split()
                # print(b)
                if (len(b) == 0):
                    continue
                elif(b[0]=='OBAMA:' or b[0]=='ROMNEY:'):
                      break
                else:
                    lehrer =lehrer+ ' '.join(b)
                    #print(' '.join(b))
print(lehrer)

"""
(15 points) Use the porter, snowball and lancaster stemmers from the nltk package to stem
each of the speaker statements.
Note: You will need to do the following preprocessing steps on the statements BEFORE you
apply the stemmers:
Discard punctuation
Remove capitalization
Remove stop words (use NLTK stopwords)
Tokenize the words
Apply each of the stemmers
"""
print("Solution to question 7 (b):::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

obama = obama.lower()
romney = romney.lower()
lehrer = lehrer.lower()
#removing punctuation
regex = re.compile('[%s]' % re.escape(string.punctuation))
obama = regex.sub('', obama)

regex = re.compile('[%s]' % re.escape(string.punctuation))
romney = regex.sub('', romney)

regex = re.compile('[%s]' % re.escape(string.punctuation))
lehrer = regex.sub('', lehrer)


stop_words = set(stopwords.words('english'))
#print(stop_words)
word_tokens_obama = word_tokenize(obama)

stop_words = set(stopwords.words('english'))
#print(stop_words)
word_tokens_romney = word_tokenize(romney)

stop_words = set(stopwords.words('english'))
#print(stop_words)
word_tokens_lehrer = word_tokenize(lehrer)

filtered_sentence_obama = [w for w in word_tokens_obama if not w in stop_words]
#print(filtered_sentence_obama)

filtered_sentence_romney = [w for w in word_tokens_romney if not w in stop_words]
#print(filtered_sentence_romney)

filtered_sentence_lehrer = [w for w in word_tokens_lehrer if not w in stop_words]
#print(filtered_sentence_lehrer)

from nltk.stem.porter import *

#stemmer = PorterStemmer()

porter = nltk.PorterStemmer()
porterStemobama =[porter.stem(t) for t in filtered_sentence_obama]
print("Obama stemmed words based on porter stemmer:::::::")
print(porterStemobama)
porterStemromney =[porter.stem(t) for t in filtered_sentence_romney]
print("Romney stemmed words  based on porter stemmer:::::")
print(porterStemromney)
porterStemlehrer =[porter.stem(t) for t in filtered_sentence_lehrer]
print("Lehrer stemmed words  based on porter stemmer::::::")
print(porterStemlehrer)

#tokens= word_tokenize(' '.join(filtered_sentence))


lancaster = nltk.LancasterStemmer()

lansporterStemobama=[lancaster.stem(t) for t in filtered_sentence_obama]
print("Obama stemmed words based on lancaster stemmer::::::")
print(lansporterStemobama)
lansStemromney=[lancaster.stem(t) for t in filtered_sentence_romney]
print("romney stemmed words based on lancaster stemmer::::::")
print(lansStemromney)
lansporterStemlehrer=[lancaster.stem(t) for t in filtered_sentence_lehrer]
print("lehrer stemmed words based on lancaster stemmer:::::")
print(lansporterStemlehrer)



from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

SnowStemobama =[stemmer.stem(t) for t in filtered_sentence_obama]
print("Obama stemmed words based on Snowball stemmer:::::::")
print(SnowStemobama)
Snowstemromney =[stemmer.stem(t) for t in filtered_sentence_romney]
print("romney stemmed words based on Snowball stemmer::::::")
print(Snowstemromney)
Snowstemlehrer =[stemmer.stem(t) for t in filtered_sentence_lehrer]
print("lehrer stemmed words based on Snowball stemmer::::::")
print(Snowstemlehrer)

"""
c. (5 points) Using the results, output the list of 10 most frequent words (stemmed) used by each
speaker separately based on each of the stems.
Note: Your output may be different from another student’s due to any differences in the way
that speaker statements are merged in part a. above. Any such differences are ok.
The above three sub-problems allow us determine which words are most often used by each
speaker. What differences do you observe between the different stemmer outputs?
"""
print("Solution to question 7 (c):::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
#Using the results, output the list of 10 most frequent words (stemmed) used by each
#speaker separately based on each of the stems.


import nltk
fdist1 = nltk.FreqDist(porterStemobama)
#print(fdist1)


print("10 most frequent words by obama porter stemmed::::::::")
print(fdist1.most_common(10))

fdist2 = nltk.FreqDist(lansporterStemobama)
#print(fdist1)
print("10 most frequent words by obama lancaster stemmed:::::::")
print(fdist2.most_common(10))

fdist1 = nltk.FreqDist(SnowStemobama)
#print(fdist1)
print("10 most frequent words by obama snowball stemmed::::::::")
print(fdist1.most_common(10))

print()

#----------------------------------------------------

fdist2 = nltk.FreqDist(porterStemromney)
#print(fdist1)

print("10 most frequent words by romney porter stemmed:::::::::::")
print(fdist2.most_common(10))

fdist1 = nltk.FreqDist(lansStemromney)
#print(fdist1)

print("10 most frequent words by romney lancaster stemmed:::::::::")
print(fdist1.most_common(10))

fdist2 = nltk.FreqDist(Snowstemromney)
#print(fdist1)

print("10 most frequent words by romney snowball stemmed::::::::::")
print(fdist2.most_common(10))

#-----------------------------------------------------
fdist1 = nltk.FreqDist(porterStemlehrer)
#print(fdist1)

print("10 most frequent words by lehrer porter stemmed:::::::::::")
print(fdist1.most_common(10))

print("10 most frequent words by lehrer lancaster stemmed:::::::::")
fdist2 = nltk.FreqDist(lansporterStemlehrer)
#print(fdist1)
print(fdist2.most_common(10))


print("10 most frequent words by lehrer snowball stemmed:::::::::::")
fdist2 = nltk.FreqDist(Snowstemlehrer)
#print(fdist1)
print(fdist2.most_common(10))

""""
(10 points) Write a function to load the dictionary of positive words provided with this
homework (positive.txt). Use the porter stemmer to stem the words in this dictionary.
"""
print("Solution to question 7 (d):::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

positive_words=[]
readfpos = open("positive.txt")
#outfile1 = open("outfile1.txt","w")
for line3 in readfpos:
    #print(line3.strip())
    positive_words.append(line3.strip())
#print(positive_words)

porter = nltk.PorterStemmer()

#tokens= word_tokenize(' '.join(filtered_sentence))

porterStemp_ositive_words =[porter.stem(t) for t in positive_words]
print("Porter Stemmed positive words::::")
print(porterStemp_ositive_words)

print("-------------------------------------")
""""
(10 points) Using the stemmed statements of each speaker from part b. above (only the porter
stemmer output), determine which speaker uses the positive words listed in the positive word
dictionary most often. Print the 10 most frequent positive words used by each speaker.
"""
print("Solution to question 7 (e):::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
stem_pos_dic =set(porterStemp_ositive_words)

obama_pos_words=[]
for w in porterStemobama:
      for x in stem_pos_dic:
            if(w==x):
                obama_pos_words.append(w)

romney_pos_words=[]
for w in porterStemromney:
      for x in stem_pos_dic:
            if(w==x):
                romney_pos_words.append(w)


lehrer_pos_words=[]
for w in porterStemlehrer:
      for x in stem_pos_dic:
            if(w==x):
                lehrer_pos_words.append(w)


print("Frequency distribution of obama postive words::::::::::")

fdist4 = nltk.FreqDist(obama_pos_words)
#print(fdist4)
print(fdist4.most_common(10))

print("Frequency distribution of romney postive words::::::::::")
fdist4 = nltk.FreqDist(romney_pos_words)
#print(fdist4)
print(fdist4.most_common(10))

print("Frequency distribution of lehrer postive words:::::::::::::")
fdist4 = nltk.FreqDist(lehrer_pos_words)
#print(fdist4)
print(fdist4.most_common(10))

#print(len(obama_pos_words))
#print(len(romney_pos_words))
#print(len(romney_pos_words))

obama_pos_words  = len(obama_pos_words)
romney_pos_words = len(romney_pos_words)
lehrer_pos_words = len(lehrer_pos_words)



print("speaker useing maximum  positive words listed in the positive word dictionary:::::::")

if(obama_pos_words > romney_pos_words):
    if(obama_pos_words>lehrer_pos_words):
        print('Obama')
    else:
        print('lehrer')
else:
    if (romney_pos_words > lehrer_pos_words):
        print('Romney')
    else:
        print('lehrer')







