import os

import math
import string
#from  import log
import operator
from nltk.util import ngrams
import nltk

from nltk import word_tokenize
from nltk.corpus import stopwords
#Finding the working directory
dir_path = os.path.dirname(os.path.realpath(__file__))
#C:\Users\Admin\PycharmProjects\Assignment4
#print(dir_path)
stop = set(stopwords.words('english'))


readf = open(dir_path+"\\"+"train.txt")
present_speaker = None
statements1 = dict()
speakerLines = dict()
line1=''

str1=''
count=0
# Reading the training corpus
for line in readf:
    a=line

#Removing the punctuations
    exclude = set(string.punctuation)
    a = ''.join(ch for ch in a if ch not in exclude)
    count=count+1
#Removing the stopwords
    b=a.split()
    #print(b)
#Finding the speaker
    speaker = b[0]
    line_pre_list = b[1:]
    line_pre =' '.join(line_pre_list)
    str1 = str1 +line_pre
    document_count = 1
# Storing the speaker and their statements in a Dictionary "statements"
# Storing the speaker and count of their lines
    present_speaker = speaker
    if present_speaker not in statements1:
        statements1[present_speaker] = ''
        speakerLines[present_speaker] = 0
    if present_speaker is not None:
        statements1[present_speaker] += line_pre
        speakerLines[present_speaker] += document_count;

# print("Dictionary 1 statements1")
#for k, v in statements1.items():
#    print(k, v)

#print("Dictionary 2 speakerLines")
#for k, v in speakerLines.items():
#   print(k, v)

#Calculating the Vocabulary size
doc_length = len(set(str1.split()))

#total no. of documents
total_no_doc = count;
print("Problem 1 (Text Classification)" )
print("Implement a Naïve Bayes classifier Implement a Naïve Bayes classifier")
classifier = dict()
line_count =0
right =0
wrong =0
readf1 = open(dir_path+"\\"+"test.txt")

fdist = dict()
speaker_lenghth = dict()
for k, v in statements1.items():
    tokens = statements1.get(k).split()
    speaker_lenghth[k]= list(ngrams(tokens,1))
    fdist[k]= nltk.FreqDist(tokens)

#print(fdist)
count_train = 0
for line in readf1:
    #right =0
    #wrong =0
    classifier.clear()
    a=line

    exclude = set(string.punctuation)
    a = ''.join(ch for ch in a if ch not in exclude)

    new_line_list = [i for i in a.lower().split() if i not in stop]
    a = ' '.join(new_line_list)

    line_count = line_count +1

    #print(a)

    count_train=count_train+1
    #print(a)
    b=a.split()
    pre_processed_doc_length = len(b)
    speaker = b[0]
    line_pre_list = b[1:]
    pre_processed_doc_length = len(line_pre_list)
    #print("line_pre_list",line_pre_list)
    #print(speaker)
    Preprocesed_line =' '.join(line_pre_list)

   # print(' '.join(b))
    Preprocesed_line =' '.join(b)
   # print(len(b))
    count=1
    for word in Preprocesed_line.split():
        for k,v in fdist.items():
            if k not in classifier:
                classifier[k] = speakerLines[k]/total_no_doc
            freq = fdist[k][word] + 1
            if k is not None:
                classifier[k] += math.log(freq)
                #uni_freq[k]
                classifier[k] -= math.log(len(speaker_lenghth[k])+doc_length)
                #classifier[k] -= math.log(len(statements1[k].split()) + doc_length)
    if not classifier:
        right = right +1
        continue

    max_keys =max(classifier.keys(), key=(lambda k: classifier[k]))
    pred_speaker = ''.join(max_keys)
    if pred_speaker==speaker:
        right = right +1
        classifier.clear()


Accuracy = right/count_train
print("Accuracy of Naïve Bayes classifier is  ",Accuracy)

import operator
#stats = {'a':1000, 'b':3000, 'c': 100}
#max(stats.iteritems(), key=operator.itemgetter(1))[0]

#print("sad")
#for k, v in statements3.items():
#   print(k, v)

print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

print("Problem 2 a (Feature Engineering)")

print("Optimizing Naïve Bayes classifier using Binary Naive Bayes classifier ")


classifier = dict()
line_count =0
right =0
wrong =0
readf1 = open(dir_path+"\\"+"test.txt")

fdist = dict()
speaker_lenghth = dict()
for k, v in statements1.items():
    tokens = statements1.get(k).split()
    speaker_lenghth[k]= list(ngrams(tokens,1))
    fdist[k]= nltk.FreqDist(tokens)

#print(fdist)
count_train = 0
for line in readf1:
    #right =0
    #wrong =0
    classifier.clear()
    a=line

    exclude = set(string.punctuation)
    a = ''.join(ch for ch in a if ch not in exclude)

    new_line_list = [i for i in a.lower().split() if i not in stop]
    a = ' '.join(new_line_list)

    line_count = line_count +1
    #print(a)

    count_train=count_train+1
    #print(a)
    b=a.split()
    pre_processed_doc_length = len(b)
    speaker = b[0]
    line_pre_list = b[1:]
    pre_processed_doc_length = len(line_pre_list)
    #print("line_pre_list",line_pre_list)
    #print(speaker)
    Preprocesed_line =' '.join(line_pre_list)

   # print(' '.join(b))
    Preprocesed_line =' '.join(b)
   # print(len(b))
    count=1
    for word in set(Preprocesed_line.split()):
        for k,v in fdist.items():
            if k not in classifier:
                classifier[k] = speakerLines[k]/total_no_doc
            freq = fdist[k][word] + 1
            if k is not None:
                classifier[k] += math.log(freq)
                #uni_freq[k]
                classifier[k] -= math.log(len(speaker_lenghth[k])+doc_length)
                #classifier[k] -= math.log(len(statements1[k].split()) + doc_length)
    if not classifier:
        right = right +1
        continue

    max_keys =max(classifier.keys(), key=(lambda k: classifier[k]))
    pred_speaker = ''.join(max_keys)
    if pred_speaker==speaker:
        right = right +1
        classifier.clear()


accuracy = right/count_train
print("Accuracy of Optimized Naïve Bayes classifier using Binary Naive Bayes classifier is :",accuracy)

print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

print("Problem 2 b (Feature Engineering)")



from nltk.corpus import stopwords
import nltk
import math
from nltk.util import ngrams

stop = set(stopwords.words("english"))


readfile3 = open(dir_path+"\\"+"train.txt")

import string

# list_speakers = set()
dataset = list(readfile3)
voc = ''
n_docs = len(dataset)
statements = dict()
class_count = dict()
for line in dataset:
    bigram_freq = dict()
    fdist = dict()
    doc_count = 1
    a = line
    exclude = set(string.punctuation)
    a = ''.join(ch for ch in a if ch not in exclude)
    s = a.split()
    speaker = s[0]
    content = (a.split(' ', 1)[1])
    voc = voc + content
    if speaker is not None:
        present_speaker = speaker
        if present_speaker not in statements:
            statements[present_speaker] = ""
        if present_speaker is not None:
            statements[present_speaker] += content
        if present_speaker not in class_count:
            class_count[present_speaker] = 0
        class_count[present_speaker] += doc_count
voc_list = list((set(voc.split())))
vocab = ' '.join(list((set(voc.split()))))
bi_vocab = list(ngrams(vocab.split(), 2))


for k, v in statements.items():
    s = statements.get(k).split()
    bigram_freq[k] = list(ngrams(s, 2))
    fdist[k] = nltk.FreqDist(bigram_freq[k])

readfile5 = open(dir_path+"\\"+"test.txt")

testset = list(readfile5)

classifier = dict()
q = 0
pred = 0

for line in testset:
    a = line
    new_line_list = [i for i in a.lower().split() if i not in stop]
    a = ' '.join(new_line_list)
    exclude = set(string.punctuation)
    a = ''.join(ch for ch in a if ch not in exclude)
    b = a.split()
    speaker = b[0]
    Preprocesed_line = ' '.join(b)
    content_list = Preprocesed_line.split()
    test_sentence = content_list[1:]
    #    test_sentence = list(set(content_list[1:]))
    for i in range(len(test_sentence)):
        if i == len(test_sentence) - 1:
            break
        for k, v in fdist.items():
            if k not in classifier:
                classifier[k] = class_count[k] / n_docs
            freq = fdist[k][(test_sentence[i], test_sentence[i + 1])] + 1
            classifier[k] += math.log(freq)
            classifier[k] -= math.log(len(bigram_freq[k]) + (doc_length*doc_length))
    if not classifier:
        pred = pred + 1
        continue
    max_keys = max(classifier.keys(), key=(lambda k: classifier[k]))
    pred_speaker = ''.join(max_keys)
    if  pred_speaker == speaker:
        right = right + 1
        classifier.clear()

accuracy = right / count_train
print("Accuracy Feature Engineering :Optimizing Naïve Bayes classifier using Bigram :" ,accuracy)



print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")








