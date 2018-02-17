from collections import defaultdict as ddict
import numpy as np


def train(eng, fr, prtable, debug=False):
    ec_num = ddict(lambda: 1e-6)
    ec_den = ddict(lambda: 1e-6)
    # E step
    if debug:
        print('E Step')
    for eSent, fSent in zip(eng, fr):
        # split the words and insert NULL word
        e = eSent.strip().split(' ')
        e.insert(0, 'NULL')
        f = fSent.strip().split(' ')
        l = len(e)
        m = len(f)
        # Calculate the expected counts for E step
        for j in range(m):
            a = np.zeros(l)
            for i in range(l):
                a[i] = prtable[f[j], e[i]]
                if debug:
                    print('Pr. Lookup:', e[i], f[j], prtable[f[j], e[i]], np.sum(a))
            a = a / np.sum(a)
            for i in range(l):
                ec_num[f[j], e[i]] += a[i]
                ec_den[e[i]] += a[i]
    # M Step
    if debug:
        print('M Step')
    for fj, ei in prtable.keys():
        # calculate p(fj|ei) table from expected counts
        prtable[fj, ei] = ec_num[fj, ei] / ec_den[ei]
        if debug:
            print(ei, fj, ec_num[fj, ei], prtable[fj, ei])
    return prtable


def readfile(filename):
    sentList = []
    with open(filename, encoding='utf8') as f:
        for aline in f:
            sentList.append(aline.strip())
    return sentList


# Run this module to apply the algorithm on a small training and test data
def runondata(train_eng, train_fra, iterNum):
    prtable = ddict(lambda: 1e-6)
    # read training data
    trainlist_eng = readfile(train_eng)
    trainlist_fra = readfile(train_fra)
    for iter in range(iterNum):
        print('Iteration #', iter + 1)
        prtable = train(trainlist_eng, trainlist_fra, prtable)
    return prtable


if __name__ == '__main__':

    print("Training the model using English and Spanish Corpus")
    # Using 10 iterations
    dic = runondata('europarl-v7.fr-en.en', 'europarl-v7.fr-en.fr', 10)
    print("Training completed")
    fr_trans = open('trans.txt', 'w')
    #    print(dic)
    test_fr = readfile('newstest2013.fr')
    print(len(test_fr))
    print("Testing Phase:")
    tmp = dict()
    import operator

    for line in test_fr:
        print("Testing new line")
        trans = ''
        words = line.split()
        for word in words:
            key = word
            for k, v in dic.items():
                if k[0] == key:
                    tmp[k[1]] = v
            if len(tmp) == 0:
                trans = trans + ' '
            else:
                trans = trans + max(tmp.items(), key=operator.itemgetter(1))[0] + ' '
            tmp.clear()
        print(trans)
        fr_trans.write(trans)
        fr_trans.write('\n')
    fr_trans.close()

