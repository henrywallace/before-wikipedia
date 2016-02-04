from collections import Counter
import nltk; from nltk.util import ngrams
from itertools import groupby, islice
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Predictor(object):
    def __init__(self):
        pass

    def urltext(self, url):
        print('retrieving text...')
        html = urlopen(url).read()
        soup = BeautifulSoup(html)
        return soup.get_text()

    def analyze(self, raw, back=2, ahead=1, normalize=str.lower):
        tokens = nltk.word_tokenize(normalize(raw))
        grams = ngrams(tokens, back + ahead)
        print('generating transitions...')
        trans = {k: Counter(t[-ahead:] for t in group).most_common() for k, group in \
            groupby(sorted(grams), key=lambda x: x[:back])} 
        return trans

    def save_tokens(self):
        pass

if __name__ == '__main__':
    p = Predictor()
    raw = p.urltext('http://www.masseiana.org/pliny.htm')
    d = p.analyze(raw)