import pandas as pd
import os
import io
from HindiTokenizer import Tokenizer

dir_path = os.path.dirname(os.path.realpath(__file__))

corpusdir = './data/' # Directory of corpus.

def raw():
    texts = []
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




