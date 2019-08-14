import nltk
from nltk.corpus import udhr
english = udhr.raw('English-Latin1')
french =  udhr.raw('French_Francais-Latin1')
italian = udhr.raw('Italian_Italiano-Latin1')
spanish = udhr.raw('Spanish_Espanol-Latin1')

english_train, english_dev =  english[0:1000], english[1000:1100]
french_train, french_dev =  french[0:1000], french[1000:1100]
italian_train, italian_dev =  italian[0:1000], italian[1000:1100]
spanish_train, spanish_dev =  spanish[0:1000], spanish[1000:1100]
english_test =  udhr.words('English-Latin1')[0:1000]
french_test =  udhr.words('French_Francais-Latin1')[0:1000]
italian_test =  udhr.words('Italian_Italiano-Latin1')[0:1000]
spanish_test =  udhr.words('Spanish_Espanol-Latin1')[0:1000]
print("::::::::::::::::::: :::::::::::::::::::::::::::Solutions to prpblem 1 ::::::::::::::::::::::::::::::::::::::::::")
# Preprocessing the  English Corpus
import string
#converting the corpus to lower case
english_train_lower = english_train.lower()
#Removing Punctuation
exclude = set(string.punctuation)
english_train_lower = ''.join(ch for ch in english_train_lower if ch not in exclude)
english_test_lower = [token.lower() for token in english_test]

# Preprocessing the French Corpus

import string
french_train_lower = french_train.lower()
exclude = set(string.punctuation)
french_train_lower = ''.join(ch for ch in french_train_lower if ch not in exclude)
french_test_lower = [token.lower() for token in french_test]

# Preprocessing the  Italian Corpus
import string
#converting the corpus to lower case
italian_train_lower = italian_train.lower()
#Removing Punctuation
exclude = set(string.punctuation)
italian_train_lower = ''.join(ch for ch in italian_train_lower if ch not in exclude)
italian_test_lower = [token.lower() for token in italian_test]

# Preprocessing the  Spanish Corpus
import string
spanish_train_lower = spanish_train.lower()
exclude = set(string.punctuation)
spanish_train_lower = ''.join(ch for ch in spanish_train_lower if ch not in exclude)
spanish_test_lower = [token.lower() for token in spanish_test]

#creating Models
print("Unigram Models:::::::::::::::::::::::::::::::::")

print("English Unigram model")
fdist_unigram_english=nltk.FreqDist(list(nltk.ngrams(english_train_lower,1)))
print(fdist_unigram_english)

print("French Unigram model")
fdist_unigram_french=nltk.FreqDist(list(nltk.ngrams(french_train_lower,1)))
print(fdist_unigram_french)

print("Italian Unigram model")
fdist_unigram_italian=nltk.FreqDist(list(nltk.ngrams(italian_train_lower,1)))
print(fdist_unigram_italian)

print("Spanish Unigram model")
fdist_unigram_spanish=nltk.FreqDist(list(nltk.ngrams(spanish_train_lower,1)))
print(fdist_unigram_spanish)
print("-----------------------------------------------------------------------------------------------------------------")

print("Bigram Models:::::::::::::::::::::::::::::::::::")

print("English bigram model")
fdist_bigram_english=nltk.FreqDist(list(nltk.bigrams(english_train_lower)))
print(fdist_bigram_english)

print("French bigram model")
fdist_bigram_french=nltk.FreqDist(list(nltk.bigrams(french_train_lower)))
print(fdist_bigram_french)

print("Italian bigram model")
fdist_bigram_italian=nltk.FreqDist(list(nltk.bigrams(italian_train_lower)))
print(fdist_bigram_italian)

print("Spanish bigram model")
fdist_bigram_spanish=nltk.FreqDist(list(nltk.bigrams(spanish_train_lower)))
print(fdist_bigram_spanish)

print("-----------------------------------------------------------------------------------------------------------------")

print("Trigram Models::::::::::::::::::::::::::::::::::::")

print("English trigram model")
fdist_trigram_english=nltk.FreqDist(list(nltk.trigrams(english_train_lower)))
print(fdist_trigram_english)

print("French trigram model")
fdist_trigram_french=nltk.FreqDist(list(nltk.trigrams(french_train_lower)))
print(fdist_trigram_french)

print("Italian trigram model")
fdist_trigram_italian=nltk.FreqDist(list(nltk.trigrams(italian_train_lower)))
print(fdist_trigram_italian)

print("Spanish trigram model")
fdist_trigram_spanish=nltk.FreqDist(list(nltk.trigrams(spanish_train_lower)))
print(fdist_trigram_spanish)

print("-----------------------------------------------------------------------------------------------------------------")

#English Unigram Accuracy with English test data

print("English Unigram Accuracy with English test data ")
count_eng = 0
for i in english_test_lower:
  english_test_unigram =list(nltk.ngrams(i,1))
  probability_english =1
  probability_french  =1

  for t in  english_test_unigram:
     probability_english = probability_english * fdist_unigram_english.freq(t)
     probability_french  = probability_french  *  fdist_unigram_french.freq(t)


  if probability_english >= probability_french:
         count_eng=count_eng+1

print("English unigram model accuracy with English test data =" +str(count_eng/len(english_test_lower)))

print("-----------------------------------------------------------------------------------------------------------------")
#English  bigram Accuracy with English test data

print("English bigram Accuracy with English test data")
count_eng=0
for i in english_test_lower:
  english_test_bigram =list(nltk.bigrams(i))
  probability_english =1
  probability_french  =1
  for t in  english_test_bigram:
     probability_english = probability_english * fdist_bigram_english.freq(t)
     probability_french  = probability_french  *  fdist_bigram_french.freq(t)


  if probability_english >= probability_french:
         count_eng=count_eng+1

print("English bigram model accuracy with English test data =" +str(count_eng/len(english_test_lower)))

print("-----------------------------------------------------------------------------------------------------------------")

#English  trigram Accuracy

print("English trigram Accuracy with English test data")
count_eng=0
for i in english_test_lower:
  english_test_trigram =list(nltk.trigrams(i))
  probability_english =1
  probability_french  =1
  for t in  english_test_trigram:
     probability_english = probability_english * fdist_trigram_english.freq(t)
     probability_french  = probability_french  *  fdist_trigram_french.freq(t)


  if probability_english >= probability_french:
         count_eng=count_eng+1

print("English trigram model accuracy with English test data =" +str(count_eng/len(english_test_lower)))

print("-----------------------------------------------------------------------------------------------------------------")

# french Accuracy
print("French Accuracy for different models")

print("French Unigram Accuracy with French test data ")
count_french = 0
for i in french_test_lower:
    french_test_unigram = list(nltk.ngrams(i, 1))
    probability_english = 1
    probability_french = 1

    for t in french_test_unigram:
        probability_english = probability_english * fdist_unigram_english.freq(t)
        probability_french = probability_french * fdist_unigram_french.freq(t)

    if probability_english <= probability_french:
        count_french = count_french + 1

print("French unigram model accuracy with French test data =" + str(count_french / len(french_test_lower)))

print("-----------------------------------------------------------------------------------------------------------------")
# French  bi Accuracy

print("French  bigram Accuracy")
count_french = 0
for i in french_test_lower:
    french_test_bigram = list(nltk.bigrams(i))
    probability_english = 1
    probability_french = 1
    for t in french_test_bigram:
        probability_english = probability_english * fdist_bigram_english.freq(t)
        probability_french = probability_french * fdist_bigram_french.freq(t)

    if probability_english <= probability_french:
        count_french = count_french + 1

print("French bigram model accuracy with French test data =" + str(count_french / len(french_test_lower)))

print("-----------------------------------------------------------------------------------------------------------------")

# French trigram Accuracy

print("French trigram Accuracy with French test data ")
count_french = 0
for i in french_test_lower:
    french_test_trigram = list(nltk.trigrams(i))
    probability_english = 1
    probability_french = 1
    for t in french_test_trigram:
        probability_english = probability_english * fdist_trigram_english.freq(t)
        probability_french = probability_french * fdist_trigram_french.freq(t)

    if probability_english <= probability_french:
        count_french = count_french + 1

print("French trigram model accuracy with French test data =" + str(count_french / len(french_test_lower)))


print(":::::::::::::::::::::::::::::::::::::::::::::Solution to question 2::::::::::::::::::::::::::::::::::::::::::::::")

# Italian  Uni Accuracy

print("Italian Unigram Accuracy with italian data ")
count_italian = 0
for i in italian_test_lower:
    italian_test_unigram = list(nltk.ngrams(i, 1))
    probability_italian = 1
    probability_spanish = 1

    for t in italian_test_unigram:
        probability_italian = probability_italian * fdist_unigram_italian.freq(t)
        probability_spanish = probability_spanish * fdist_unigram_spanish.freq(t)

    if probability_italian >= probability_spanish:
        count_italian = count_italian + 1

print("Italian unigram model accuracy with italian data=" + str(count_italian / len(italian_test_lower)))

print("-----------------------------------------------------------------------------------------------------------------")


print("Italian bigram Accuracy with italian data")
count_italian = 0
for i in italian_test_lower:
    italian_test_bigram = list(nltk.bigrams(i))
    probability_italian = 1
    probability_spanish = 1
    for t in italian_test_bigram:
        probability_italian = probability_italian * fdist_bigram_italian.freq(t)
        probability_spanish = probability_spanish * fdist_bigram_spanish.freq(t)

    if probability_italian >= probability_spanish:
        count_italian = count_italian + 1

print("Italian bigram model accuracy with italian data =" + str(count_italian / len(italian_test_lower)))

print("-----------------------------------------------------------------------------------------------------------------")



print("Italian trigram Accuracy with italian data")
count_italian = 0
for i in italian_test_lower:
    italian_test_trigram = list(nltk.trigrams(i))
    probability_italian = 1
    probability_spanish = 1
    for t in italian_test_trigram:
        probability_italian = probability_italian * fdist_trigram_italian.freq(t)
        probability_spanish = probability_spanish * fdist_trigram_spanish.freq(t)

    if probability_italian >= probability_spanish:
        count_italian = count_italian + 1

print("Italian trigram model accuracy with italian data=" + str(count_italian / len(italian_test_lower)))

print("-----------------------------------------------------------------------------------------------------------------")



# Spanish Accuracy

print("Spanish Unigram Accuracy with spanish data")
count_spanish = 0
for i in spanish_test_lower:
    spanish_test_unigram = list(nltk.ngrams(i, 1))
    probability_italian = 1
    probability_spanish = 1

    for t in spanish_test_unigram:
        probability_italian = probability_italian * fdist_unigram_italian.freq(t)
        probability_spanish = probability_spanish * fdist_unigram_spanish.freq(t)

    if probability_italian <= probability_spanish:
        count_spanish = count_spanish + 1

print("Spanish unigram model accuracy with spanish data=" + str(count_spanish / len(spanish_test_lower)))



print("-----------------------------------------------------------------------------------------------------------------")


print("Spanish bigram Accuracy  with spanish data")
count_spanish = 0
for i in spanish_test_lower:
    spanish_test_bigram = list(nltk.bigrams(i))
    probability_italian = 1
    probability_spanish = 1
    for t in spanish_test_bigram:
        probability_italian = probability_italian * fdist_bigram_italian.freq(t)
        probability_spanish = probability_spanish * fdist_bigram_spanish.freq(t)

    if probability_italian <= probability_spanish:
        count_spanish = count_spanish + 1

print("Spanish bigram model accuracy  with spanish data=" + str(count_spanish / len(spanish_test_lower)))

print("-----------------------------------------------------------------------------------------------------------------")


print("spanish trigram Accuracy with spanish data")
count_spanish = 0
for i in spanish_test_lower:
    spanish_test_trigram = list(nltk.trigrams(i))
    probability_italian = 1
    probability_spanish = 1
    for t in spanish_test_trigram:
        probability_italian = probability_italian * fdist_trigram_italian.freq(t)
        probability_spanish = probability_spanish * fdist_trigram_spanish.freq(t)

    if probability_italian <= probability_spanish:
        count_spanish = count_spanish + 1

print("Spanish trigram model accuracy with spanish data=" + str(count_spanish / len(spanish_test_lower)))

print("----------------------------------------------End-------------------------------------------------------------------")
