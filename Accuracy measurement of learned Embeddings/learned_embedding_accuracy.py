import os
os.getcwd()

#glove2word2vec

# Solution to Problem 1

# Source of Embeddings :- http://nlp.stanford.edu/projects/glove/
print("Source of Embeddings :- http://nlp.stanford.edu/projects/glove/")
# Case 1 N(Dimension of vector) = 50
print(" Case 1 N(Dimension of vector) = 50")
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
glove_input_file = os.getcwd()+"\\"+"glove.6B.50d.txt"
word2vec_output_file = 'glove.6B.50d.txt.word2vec'
#Converting the GloVe file format to the word2vec file format.
#glove2word2vec() function is used to convert GloVe file format to the word2vec file format
glove2word2vec(glove_input_file, word2vec_output_file)
#filename: glove.6B.50d.txt.word2vec contains GloVe model in word2vec format.
#Creating/loading a model load_word2vec_format 
#Converted file is ASCII format, not binary, so we set binary=False when loading.
model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)
#Testing the accuracy of the Model using accuracy method
model.accuracy(os.getcwd()+"\\"+"word-test.v1.txt")
print(model.accuracy(os.getcwd()+"\\"+"word-test.v1.txt"))
model.most_similar("increase")
print(model.most_similar("increase"))



# Case 2 N(Dimension of vector) = 100
print(" Case 2 N(Dimension of vector) = 100")
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
glove_input_file = os.getcwd()+"\\"+"glove.6B.100d.txt"
word2vec_output_file = 'glove.6B.100d.txt.word2vec'
#Converting the GloVe file format to the word2vec file format.
#glove2word2vec() function is used to convert GloVe file format to the word2vec file format
glove2word2vec(glove_input_file, word2vec_output_file)
#filename: glove.6B.100d.txt.word2vec contains GloVe model in word2vec format.
#Creating/loading a model load_word2vec_format 
#Converted file is ASCII format, not binary, so we set binary=False when loading.
model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)
#Testing the accuracy of the Model using accuracy method
model.accuracy(os.getcwd()+"\\"+"word-test.v1.txt")
print(model.accuracy(os.getcwd()+"\\"+"word-test.v1.txt"))
print(model.most_similar("increase"))



# Case 2 N(Dimension of vector) = 200
print(" Case 3 N(Dimension of vector) = 200")
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
glove_input_file = os.getcwd()+"\\"+"glove.6B.200d.txt"
word2vec_output_file = 'glove.6B.200d.txt.word2vec'
#Converting the GloVe file format to the word2vec file format.
#glove2word2vec() function is used to convert GloVe file format to the word2vec file format
glove2word2vec(glove_input_file, word2vec_output_file)
#filename: glove.6B.200d.txt.word2vec contains GloVe model in word2vec format.
#Creating/loading a model load_word2vec_format 
#Converted file is ASCII format, not binary, so we set binary=False when loading.
model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)
#Testing the accuracy of the Model using accuracy method
model.accuracy(os.getcwd()+"\\"+"word-test.v1.txt")
print(model.accuracy(os.getcwd()+"\\"+"word-test.v1.txt"))
print(model.most_similar("increase"))



# Case 2 N(Dimension of vector) = 300
print(" Case 4 N(Dimension of vector) = 300")
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
glove_input_file = os.getcwd()+"\\"+"glove.6B.300d.txt"
word2vec_output_file = 'glove.6B.300d.txt.word2vec'
#Converting the GloVe file format to the word2vec file format.
#glove2word2vec() function is used to convert GloVe file format to the word2vec file format
glove2word2vec(glove_input_file, word2vec_output_file)
#filename: glove.6B.300d.txt.word2vec contains GloVe model in word2vec format.
#Creating/loading a model load_word2vec_format 
#Converted file is ASCII format, not binary, so we set binary=False when loading.
model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)
#Testing the accuracy of the Model using accuracy method
model.accuracy(os.getcwd()+"\\"+"word-test.v1.txt")
print(model.accuracy(os.getcwd()+"\\"+"word-test.v1.txt"))
print(model.most_similar("increase"))


# mattmahoney.net with text8.txt and enwik9.txt


print("#mattmahoney.net with text8.txt")
#mattmahoney.net
# Using text8.txt
from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# load up unzipped corpus from http://mattmahoney.net/dc
sentences = word2vec.Text8Corpus(os.getcwd()+"\\"+"text8.txt")
# train the skip-gram model; default window=5
model = word2vec.Word2Vec(sentences, size=200)
# Calculating the accuracy of the model using model.accuracy
model.accuracy(os.getcwd()+"\\"+"word-test.v1.txt")
print(model.accuracy(os.getcwd()+"\\"+"word-test.v1.txt"))
print(model.most_similar("increase"))



#mattmahoney.net
#enwik9.txt
print("#mattmahoney.net with enwik9.txt")
from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#>>> # load up unzipped corpus from http://mattmahoney.net/dc/ 
# used enwik9.zip
sentences = word2vec.Text8Corpus(os.getcwd()+"\\"+"enwik9.txt")
# train the skip-gram model; default window=5
#model = word2vec.Word2Vec(sentences, size=200)
model = word2vec.Word2Vec(sentences, size=200)
# Usung accuracy function on model to calculate Accuarcy for given test data.
model.accuracy(os.getcwd()+"\\"+"word-test.v1.txt")
print(model.accuracy(os.getcwd()+"\\"+"word-test.v1.txt"))
print(model.most_similar("increase"))

# Solution to problem 3

#glove2word2vec



#  Source of Embeddings :- http://nlp.stanford.edu/projects/glove/
print("Calculating Accuracy with my own test file with Glove N(Dimension of vector) = 50 ")
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
glove_input_file = os.getcwd()+"\\"+"glove.6B.50d.txt"
word2vec_output_file = 'glove.6B.50d.txt.word2vec'
#Converting the GloVe file format to the word2vec file format.
#glove2word2vec() function is used to convert GloVe file format to the word2vec file format
glove2word2vec(glove_input_file, word2vec_output_file)
#filename: glove.6B.50d.txt.word2vec contains GloVe model in word2vec format.
#Creating/loading a model load_word2vec_format 
#Converted file is ASCII format, not binary, so we set binary=False when loading.
model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)
#Testing the accuracy of the Model using accuracy method
model.accuracy(os.getcwd()+"\\"+"Test3.txt")
print(model.accuracy(os.getcwd()+"\\"+"Test3.txt"))

print("Calculating Accuracy with my own test file with Glove N(Dimension of vector) = 100 ")
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
glove_input_file = os.getcwd()+"\\"+"glove.6B.100d.txt"
word2vec_output_file = 'glove.6B.100d.txt.word2vec'
#Converting the GloVe file format to the word2vec file format.
#glove2word2vec() function is used to convert GloVe file format to the word2vec file format
glove2word2vec(glove_input_file, word2vec_output_file)
#filename: glove.6B.100d.txt.word2vec contains GloVe model in word2vec format.
#Creating/loading a model load_word2vec_format 
#Converted file is ASCII format, not binary, so we set binary=False when loading.
model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)
#Testing the accuracy of the Model using accuracy method
model.accuracy(os.getcwd()+"\\"+"Test3.txt")
print(model.accuracy(os.getcwd()+"\\"+"Test3.txt"))

print("Calculating Accuracy with my own test file with Glove N(Dimension of vector) = 200 ")
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
glove_input_file = os.getcwd()+"\\"+"glove.6B.200d.txt"
word2vec_output_file = 'glove.6B.200d.txt.word2vec'
#Converting the GloVe file format to the word2vec file format.
#glove2word2vec() function is used to convert GloVe file format to the word2vec file format
glove2word2vec(glove_input_file, word2vec_output_file)
#filename: glove.6B.200d.txt.word2vec contains GloVe model in word2vec format.
#Creating/loading a model load_word2vec_format 
#Converted file is ASCII format, not binary, so we set binary=False when loading.
model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)
#Testing the accuracy of the Model using accuracy method
model.accuracy(os.getcwd()+"\\"+"Test3.txt")
print(model.accuracy(os.getcwd()+"\\"+"Test3.txt"))


print("Calculating Accuracy with my own test file with Glove N(Dimension of vector) = 300 ")
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
glove_input_file = os.getcwd()+"\\"+"glove.6B.300d.txt"
word2vec_output_file = 'glove.6B.300d.txt.word2vec'
#Converting the GloVe file format to the word2vec file format.
#glove2word2vec() function is used to convert GloVe file format to the word2vec file format
glove2word2vec(glove_input_file, word2vec_output_file)
#filename: glove.6B.300d.txt.word2vec contains GloVe model in word2vec format.
#Creating/loading a model load_word2vec_format 
#Converted file is ASCII format, not binary, so we set binary=False when loading.
model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)
#Testing the accuracy of the Model using accuracy method
model.accuracy(os.getcwd()+"\\"+"Test3.txt")
print(model.accuracy(os.getcwd()+"\\"+"Test3.txt"))


# mattmahoney.net with text8.txt and enwik9.txt


print(" Calculating Accuracy with my own test file #mattmahoney.net with text8.txt")
#mattmahoney.net
# Using text8.txt
from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# load up unzipped corpus from http://mattmahoney.net/dc
sentences = word2vec.Text8Corpus(os.getcwd()+"\\"+"text8.txt")
# train the skip-gram model; default window=5
model = word2vec.Word2Vec(sentences, size=200)
# Calculating the accuracy of the model using model.accuracy
model.accuracy(os.getcwd()+"\\"+"Test3.txt")
print(model.accuracy(os.getcwd()+"\\"+"Test3.txt"))



#mattmahoney.net
#enwik9.txt
print("Calculating Accuracy with my own test file #mattmahoney.net with enwik9.txt")
from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#>>> # load up unzipped corpus from http://mattmahoney.net/dc/ 
# used enwik9.zip
sentences = word2vec.Text8Corpus(os.getcwd()+"\\"+"enwik9.txt")
# train the skip-gram model; default window=5
#model = word2vec.Word2Vec(sentences, size=200)
model = word2vec.Word2Vec(sentences, size=200)
# Usung accuracy function on model to calculate Accuarcy for given test data.
model.accuracy(os.getcwd()+"\\"+"Test3.txt")
print(model.accuracy(os.getcwd()+"\\"+"Test3.txt"))



