# -*- coding: UTF-8 -*-
import numpy as np
import string
import cPickle as pickle

def line2vec(line):
    line_info=line.split(' ')
    word=line_info[0]
    vector=np.zeros((1,300),dtype=float)
    for i in range(0,300):
        vector[0,i]=string.atof(line_info[i+1])
    return word,vector

with open('wiki.zh.vec','r') as f:
    vectors=f.readlines()
    n=100000
    words=[]
    words2vectors=np.ndarray((n,300),dtype=float)
    for i in range(0,n):
        words_temp,words2vectors[i,:]=line2vec(vectors[i+1])
        words.append(words_temp)
    # print words[0],words2vectors[0,:]
    fpkl=file('zh_vec_fb.pkl', 'w')
    pickle.dump((words,words2vectors),fpkl)



