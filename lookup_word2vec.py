# -*- coding: UTF-8 -*-
import numpy as np
import cPickle as pickle
import re

def strdecode(sentence):
    if not isinstance(sentence, unicode):
        try:
            sentence = sentence.decode('utf-8')
        except UnicodeDecodeError:
            sentence = sentence.decode('gbk', 'ignore')
    return sentence

def word2vec(word):
    vec=np.zeros((1,300),dtype=float)
    f=open('zh_vec.pkl','r')
    v=pickle.load(f)
    f.close()
    f=open('zh_dict','r')
    dict=f.readlines()
    f.close()
    i=0
    word=strdecode(word)
    pattern=u'%s'%word
    for dict_n in range(0,len(dict)):
        dict_word=strdecode(dict[dict_n])
        if re.search(pattern,dict_word):
            vec=v[dict_n,:]
            break
    return vec