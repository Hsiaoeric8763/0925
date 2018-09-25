import nltk, collections

from nltk.collocations import BigramCollocationFinder
from nltk.util import ngrams
from  nltk.metrics import BigramAssocMeasures

def ngram_probs(filename='raw_sentences.txt'):
    content = open(filename,'r').read()
    token = content.lower().split()

    bigrams = ngrams(token,2)
    bigramcount = collections.Counter(bigrams)

    tigrams = ngrams(token,3)
    tigramcount = collections.Counter(tigrams)
    return bigramcount, tigramcount
    
    


if __name__ == '__main__':
     cnt2, cnt3= ngram_probs()
     print(cnt2, cnt3)
