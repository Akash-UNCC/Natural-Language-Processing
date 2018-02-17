import nltk
import os
# Creating a dictionary with contains german words and corresponding English meaning as a key value pair
conversion = dict()
# Opening two files simultaneously and reading and reading it with Zip
with open(os.getcwd() + "\\" + "germany.txt", encoding="utf8") as germany, open(os.getcwd() + "\\" + "english.txt", encoding = "utf8") as english:
    for x, y in zip(germany, english):
        #preprocessing the german - english words before storing in dictionary
        x = x.replace("\n", "").strip().replace(u'\ufeff', '')
        y = y.replace("\n", "").strip().replace(u'\ufeff', '')
        conversion[x] = y
#print(d)
# Reading 5 sentences from an external files with contains 5 German sentences
print("# Reading 5 sentences from an external files with contains 5 German sentences")
germanSentences = []
germanTestSentences = open(os.getcwd() + "\\" + "germanytest5sen.txt", encoding="utf8")
for sentence in germanTestSentences:
    germanSentences.append(sentence)

translate = open('transGermanToEngfile_v1.txt', 'w')
for sentence in germanSentences:
    transGermanToEng = ''
    for word in sentence.split():
        meaning = conversion.get(word.replace(u'\ufeff', ''))
        if type(meaning) == str:
            transGermanToEng = transGermanToEng + meaning + ' '
    print("translated Output = ", transGermanToEng)
    translate.write(transGermanToEng)
    translate.write('\n')
translate.close()

translation = open('transGermanToEngfile_v1.txt', 'r')
posList = []
for sentences in translation:
    tokens = nltk.word_tokenize(sentences)
    print(tokens)
    pos_tags = nltk.pos_tag(tokens)
    print(pos_tags)
    posList.append(pos_tags)

improved_translated_file = open('improvedTransGermanToEngfile1_v2.txt', 'w')
for lines in posList:
    line=lines
    # Strategy 1 : Check the and placing vowels according the English grammar rules
    print(" Strategy 1 : Check the and placing vowels according the English grammar rules")
    for i in range(0, len(line)):
        c = line[i]
        if c[0] == 'a' and i < len(line) - 1:
            nxt = line[i + 1]
            # checking the first charter if it is vowel
            if nxt[0][0] in ('a', 'e', 'i', 'o', 'u'):
                line[i] = ('an', 'DT')
        if c[0] == 'an' and i < len(line) - 1:
            nxt = line[i + 1]
            if nxt[0][0] in ('a', 'e', 'i', 'o', 'u') is False:
                line[i] = ('a', 'DT')

    # Strategy 2 : Removing any articles or determiners before a proper noun
    print(" Strategy 2 : Removing any articles or determiners before a proper noun")
    art_prop_noun_removed = []
    for i in range(0, len(line)):
        c = line[i]
        # print 'curr = ', curr
        if c[1] == 'DT' and i != len(line) - 1:
            next = line[i + 1]
            if next[1] == 'NNP' or next[1] == 'NNPS' is False:
                art_prop_noun_removed.append(c)
        else:
            art_prop_noun_removed.append(c)

    line = art_prop_noun_removed

    #Strategy 3 : Removing consecutive words if they are same
    print(" Strategy 3 : Removing consecutive words if they are same")

    adjacent_repeated_removed= []
    adjacent_repeated_removed.append(line[0])
    for i in range(1, len(line)):
        c = line[i]
        p = line[i - 1]
        if c[0] == p[0]:
           print("")
        else:
            adjacent_repeated_removed.append(c)

    line = adjacent_repeated_removed

    #object_follows_verbs(line):
    # Strategy 4 : All Verbs should be followed by objects
    print(" Strategy 4 : All Verbs should be followed by objects")
    restructure = []
    i = 0
    while i < len(line):
        ct = line[i]
        cw = ct[0]
        if ct[1] == 'PRP':
            nt = line[i + 1]
            nw = nt[0]
            if nt[1] == 'VB' or nt[1] == 'VBD' or nt[1] == 'VBG':
                print(cw + ' ' + nw)
                restructure.append(nt)
                restructure.append(ct)
                i += 1
        else:
            restructure.append(line[i])
        i += 1
    line = restructure



    # Strategy 5: Adjective gshould be followed by Noun
    print("Strategy 6: Adjective should be followed by Noun")
    for i in range(1, len(line)):
            c  = line[i]
            p = line[i - 1]
            if p[1] == 'NN' or p[1] == 'NNS' or p[1] == 'NNP' and c[1] == 'JJ':
                line[i - 1] = c
                line[i] = p


    # Strategy 6 : All Verbs should be followed by objects
    print(" Strategy 6 : All Verbs should be followed by objects")
    restructure = []
    i = 0
    while i < len(line):
            ct = line[i]
            cw = ct[0]
            if ct[1] == 'PRP':
                nt = line[i + 1]
                nw = nt[0]
                if nt[1] == 'VB' or nt[1] == 'VBD' or nt[1] == 'VBG':
                    print(cw + ' ' + nw)
                    restructure.append(nt)
                    restructure.append(ct)
                    i += 1
            else:
                restructure.append(line[i])
            i += 1

    line = restructure

    # Writing the processed file into a new file improvedTransGermanToEngfile1_v2
    print("Writing the processed file into a new file improvedTransGermanToEngfile1_v2")
    for l in line:
        improved_translated_file.write(l[0] + ' ')
    improved_translated_file.write('\n')
improved_translated_file.close()







