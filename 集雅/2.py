import math
import nltk
from nltk.util import ngrams
def calc_count(text):
    token = text.split()
    unigram_count = {}
    bigram_count = {}
    trigram_count = {}
    unigram = {}
    bigram = {}
    trigram = {}
    uni_count = 0

    for word in token:
        uni_count += 1
        if word in unigram:
            unigram[word] += 1
        else:
            unigram[word] = 1
    bigrams = ngrams(token,2)
    bigram_tuples = tuple(bigrams)
    for item in bigram_tuples:
            if item in bigram:
                bigram[item] += 1
            else:
                bigram[item] = 1
    
    trigrams = ngrams(token,3)
    trigram_tuples = tuple(trigrams)
    for item in trigram_tuples:
            if item in bigram:
                trigram[item] += 1
            else:
                trigram[item] = 1
  
    for word in unigram:
        temp = [word]
        unigram_count[tuple(temp)] = math.log(float(unigram[word])/uni_count)
   
    for word in bigram:
            bigram_count[tuple(word)] = math.log(float(bigram[word])/unigram[word[0]])
   
    for word in trigram:
            trigram_count[tuple(word)] = math.log(float(trigram[word])/bigram[(word[0], word[1])])
   
    return unigram_count, bigram_count, trigram_count

def prob3(unigrams, bigrams, trigrams):
    
    outfile = open('count.txt', 'w')
    for unigram in unigrams:
        outfile.write('UNIGRAM ' + unigram[0] + '/' + str(unigrams[unigram]) + '\n')
    for bigram in bigrams:
        outfile.write('BIGRAM ' + bigram[0] + '/' + bigram[1]  + ' ' + str(bigrams[bigram]) + '\n')
    for trigram in trigrams:
        outfile.write('TRIGRAM ' + trigram[0] + '/' + trigram[1] + ' ' + trigram[2] + ' ' + str(trigrams[trigram]) + '\n')
    outfile.close()

if __name__ == '__main__':
    f = open('raw_sentences.txt','r')
    content = f.read()
    text = content.lower()
    f.close()
   
    unigrams, bigrams, trigrams = calc_count(text)
    prob3(unigrams, bigrams, trigrams)
    