import pandas as pd
import os
import io
from HindiTokenizer import Tokenizer
from pydub import AudioSegment
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))

corpusdir = './data/' # Directory of corpus.

def raw(fileid = None):
    texts = []

    if fileid:
        file_text = io.open(corpusdir + fileid, "r", encoding="utf-8")
        texts.append(file_text.read())
    else:
        for file in fileids():
            file_text = io.open(corpusdir + file, "r", encoding="utf-8")
            texts.append(file_text.read())

    return texts

def fileids():
    files_ret = []
    for dir in os.listdir(corpusdir):
        try:
            files = os.listdir(corpusdir + dir + "/")
            for file in files:
                files_ret.append(dir + "/" + file)
        except:
            print("")

    return files_ret

def fileids_search(search_text):
    files_ret = []
    for dir in os.listdir(corpusdir):
        try:
            files = os.listdir(corpusdir + dir + "/")
            for file in files:
                file_text = io.open(corpusdir + dir + "/" + file, "r", encoding="utf-8")
                if search_text in file_text.read():
                    files_ret.append(dir + "/" + file)
        except:
            print("")

    return files_ret

def tokenize(fileid = None, remove_stopwords = False):
    token_list = []
    for text in raw(fileid):
        t = Tokenizer(text)
        t.tokenize()
        if remove_stopwords:
            t.remove_stop_words()
            token_list.append(t.final_tokens)
        else:
            token_list.append(t.tokens)

    return token_list

def sent_tokenize(fileid = None):
    token_list = []
    for text in raw(fileid):
        t = Tokenizer(text)
        t.generate_sentences()
        token_list.append(t.sentences)

    return token_list

#Helper function to detect silence regions
def ratio(sample):
    counter = 0
    for i in sample:
        if i <= 1 and i >=-1:
            counter+=1
    return counter/len(sample)

def get_new_sentence_locations(filename):
    speech = AudioSegment.from_file(filename)
    length = len(speech)/1000
    silence_timings = []

    for i in range(int(length)):
        sample = speech[i*1000 : (i+1)*1000].get_array_of_samples()
        sample = np.array(sample)
    
        silence = ratio(sample) > 0.05
    
        if silence:
            silence_timings.append(i)

    fullstop_timings = silence_timings

    if 0 in fullstop_timings:
        fullstop_timings.remove(0)

    for i in silence_timings[::-1]:
        for deviation in [1,2,3,4]:
            if i-deviation in fullstop_timings:
                fullstop_timings.remove(i-deviation)
    
    return fullstop_timings

def play(filename):
    return AudioSegment.from_file(filename)

#Sentences are 0 indexed
def play_sentence(filename, sentence_number):
    audio = play(filename)

    if sentence_number == 0:
        return audio
    else:
        start = get_new_sentence_locations(filename)[sentence_number]
        return audio[start*1000:]

