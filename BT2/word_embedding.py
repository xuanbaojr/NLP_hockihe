# Chuan bi du lieu
import os
import pandas as pd
import string
from pyvi import ViTokenizer
from gensim.models import Word2Vec

path_data = "./datatrain.txt"

def read_data(path):
    traindata = []
    sents = open(path, 'r', encoding="utf8").readlines()
    for sent in sents:
        traindata.append(sent.split())

    return traindata

if __name__ == '__main__':
    train_data = read_data(path_data)
    model = Word2Vec(train_data, vector_size=150, window = 10, min_count = 2, workers = 4, sg = 0)
    model.wv.save("./model/word2vec_skipgram.model")