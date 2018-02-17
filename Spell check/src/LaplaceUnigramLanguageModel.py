import collections,math
class LaplaceUnigramLanguageModel:

    def __init__(self, corpus):
      self.LaplaceunigramCounts = collections.defaultdict(lambda: 0)
      self.total = 0
      self.train(corpus)

    def train(self, corpus):
      """Takes a HolbrookCorpus corpus, does whatever training is needed. """
      for sentence in corpus.corpus:
        for datum in sentence.data:
          token = datum.word
          self.LaplaceunigramCounts[token] = self.LaplaceunigramCounts[token] + 1
          self.total += 1


    def score(self, sentence):
      """Takes a list of strings, returns a score of that sentence."""
      score = 0.0
      for token in sentence:
        # adding one for add-one smoothing
        count = self.LaplaceunigramCounts[token]+1
        score += math.log(count)
        score -= math.log(self.total+len(self.LaplaceunigramCounts))
      return score